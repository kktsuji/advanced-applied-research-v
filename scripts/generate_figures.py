"""
大学レポート用 図表生成スクリプト
出力先: docs/figs/
"""
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import os

matplotlib.rcParams['font.family'] = ['DejaVu Sans', 'sans-serif']
matplotlib.rcParams['figure.dpi'] = 150

OUTPUT_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'docs', 'figs')
os.makedirs(OUTPUT_DIR, exist_ok=True)


def fig3_phase_comparison():
    """図3: フェーズ別工数比較（AI有/無）"""
    phases = [
        'Tech\nLearning',
        'Requirements',
        'Design',
        'Implementation',
        'Testing',
        'Documentation'
    ]
    without_ai = [2.4, 3.3, 7.5, 22.5, 11.0, 10.0]
    with_ai = [0.5, 1.5, 2.5, 7.0, 3.5, 0.0]

    x = np.arange(len(phases))
    width = 0.35

    fig, ax = plt.subplots(figsize=(10, 6))
    bars1 = ax.bar(x - width/2, without_ai, width, label='Without AI (estimated)', color='#d32f2f', alpha=0.8)
    bars2 = ax.bar(x + width/2, with_ai, width, label='With AI (actual)', color='#1976d2', alpha=0.8)

    ax.set_ylabel('Person-months', fontsize=12)
    ax.set_title('Figure 3: Phase-wise Effort Comparison (With/Without AI)', fontsize=13, fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels(phases, fontsize=10)
    ax.legend(fontsize=11)
    ax.set_ylim(0, 26)

    # Add reduction % labels (positioned above value labels to avoid overlap)
    for i, (wo, wi) in enumerate(zip(without_ai, with_ai)):
        reduction = int((1 - wi/wo) * 100) if wo > 0 else 100
        label_y = wi + 1.2 if wi > 0 else 0.8
        ax.annotate(f'-{reduction}%', xy=(x[i] + width/2, label_y),
                    ha='center', fontsize=9, color='#1976d2', fontweight='bold')

    # Add value labels on bars
    for bar in bars1:
        h = bar.get_height()
        ax.annotate(f'{h:.1f}', xy=(bar.get_x() + bar.get_width()/2, h),
                    xytext=(0, 3), textcoords='offset points', ha='center', fontsize=8)
    for bar in bars2:
        h = bar.get_height()
        if h > 0:
            ax.annotate(f'{h:.1f}', xy=(bar.get_x() + bar.get_width()/2, h),
                        xytext=(0, 3), textcoords='offset points', ha='center', fontsize=8)

    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'phase_comparison.png'))
    plt.close()
    print('Generated: phase_comparison.png')


def fig4_test_ratio():
    """図4: テスト対コード比の業界比較"""
    categories = [
        'Enterprise\n(average)',
        'Quality-focused\nprojects',
        'This Project',
        'Safety-critical\n(aviation)'
    ]
    ratios = [0.4, 0.65, 1.16, 1.5]
    colors = ['#90a4ae', '#90a4ae', '#1976d2', '#90a4ae']

    fig, ax = plt.subplots(figsize=(8, 5))
    bars = ax.bar(categories, ratios, color=colors, alpha=0.85, edgecolor='white', linewidth=1.5)

    ax.set_ylabel('Test-to-Code Ratio', fontsize=12)
    ax.set_title('Figure 4: Test-to-Code Ratio - Industry Comparison', fontsize=13, fontweight='bold')
    ax.set_ylim(0, 2.0)
    ax.axhline(y=1.0, color='#e0e0e0', linestyle='--', linewidth=1)
    ax.text(3.5, 1.02, 'test lines = production lines', fontsize=8, color='gray')

    for bar, ratio in zip(bars, ratios):
        ax.annotate(f'{ratio:.2f}:1', xy=(bar.get_x() + bar.get_width()/2, bar.get_height()),
                    xytext=(0, 5), textcoords='offset points', ha='center', fontsize=11, fontweight='bold')

    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'test_ratio_comparison.png'))
    plt.close()
    print('Generated: test_ratio_comparison.png')


def fig5_maturity_progression():
    """図5: プロセス成熟度の変化（仕様量の推移）"""
    features = ['no01', 'no02', 'no03', 'no04', 'no05', 'no06',
                'no07', 'no08/09', 'no10', 'no11', 'no12']
    spec_lines = [17868, 11372, 2491, 4379, 6151, 2499,
                  2823, 1800, 1500, 10646, 809]
    # Normalize test ratios from code quality report
    test_ratios = [1.32, 1.18, 1.24, 0.65, 0.21, 0.49,
                   0.75, 1.02, 0.80, 1.17, 1.20]

    fig, ax1 = plt.subplots(figsize=(10, 5))

    color1 = '#1976d2'
    ax1.bar(features, spec_lines, color=color1, alpha=0.6, label='Spec document lines')
    ax1.set_xlabel('Feature (development order)', fontsize=11)
    ax1.set_ylabel('Specification Lines', color=color1, fontsize=11)
    ax1.tick_params(axis='y', labelcolor=color1)
    ax1.set_ylim(0, 20000)

    ax2 = ax1.twinx()
    color2 = '#d32f2f'
    ax2.plot(features, test_ratios, color=color2, marker='o', linewidth=2, markersize=6, label='Test ratio')
    ax2.set_ylabel('Test-to-Code Ratio', color=color2, fontsize=11)
    ax2.tick_params(axis='y', labelcolor=color2)
    ax2.set_ylim(0, 1.6)
    ax2.axhline(y=1.0, color=color2, linestyle='--', linewidth=0.8, alpha=0.5)

    ax1.set_title('Figure 5: Process Maturity - Spec Volume vs Code Quality', fontsize=13, fontweight='bold')

    # Annotations
    ax1.annotate('Early: detailed exploration', xy=(0, 17868), xytext=(2, 16000),
                 arrowprops=dict(arrowstyle='->', color='gray'), fontsize=9, color='gray')
    ax1.annotate('Late: efficient routine', xy=(10, 809), xytext=(7, 4000),
                 arrowprops=dict(arrowstyle='->', color='gray'), fontsize=9, color='gray')

    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'maturity_progression.png'))
    plt.close()
    print('Generated: maturity_progression.png')


if __name__ == '__main__':
    fig3_phase_comparison()
    fig4_test_ratio()
    fig5_maturity_progression()
    print(f'\nAll figures saved to: {OUTPUT_DIR}')
