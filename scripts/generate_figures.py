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


def fig3_tool_positioning():
    """図3: 仕様駆動開発ツールの位置づけ（重厚さ × 仕様の生命性）"""
    tools = ['Tessl', 'Kiro', 'spec-kit', 'OpenSpec']
    x = [0.40, 0.35, 0.75, 0.55]
    y = [0.85, 0.55, 0.30, 0.28]
    colors = ['#7b1fa2', '#f57c00', '#1976d2', '#388e3c']
    # Per-tool label offsets in points (dx, dy)
    label_offsets = [(-45, 8), (12, 8), (12, 8), (12, 8)]

    fig, ax = plt.subplots(figsize=(8, 7))

    # Quadrant backgrounds
    ax.fill_between([0.5, 1.0], 0.5, 1.0, color='#e3f2fd', alpha=0.35)
    ax.fill_between([0, 0.5], 0.5, 1.0, color='#fff3e0', alpha=0.35)
    ax.fill_between([0, 0.5], 0, 0.5, color='#f3e5f5', alpha=0.35)
    ax.fill_between([0.5, 1.0], 0, 0.5, color='#e8f5e9', alpha=0.35)

    # Quadrant dividing lines
    ax.axhline(y=0.5, color='#9e9e9e', linewidth=1)
    ax.axvline(x=0.5, color='#9e9e9e', linewidth=1)

    # Quadrant labels (corners)
    ax.text(0.97, 0.97, 'Heavy & Synced', ha='right', va='top',
            fontsize=10, color='#555', style='italic')
    ax.text(0.03, 0.97, 'Light & Synced', ha='left', va='top',
            fontsize=10, color='#555', style='italic')
    ax.text(0.03, 0.03, 'Light & Static', ha='left', va='bottom',
            fontsize=10, color='#555', style='italic')
    ax.text(0.97, 0.03, 'Heavy & Static', ha='right', va='bottom',
            fontsize=10, color='#555', style='italic')

    # Plot points and labels
    for tool, xi, yi, color, offset in zip(tools, x, y, colors, label_offsets):
        ax.scatter(xi, yi, s=400, color=color, alpha=0.85,
                   edgecolor='white', linewidth=2, zorder=3)
        ax.annotate(tool, (xi, yi), xytext=offset,
                    textcoords='offset points',
                    fontsize=12, fontweight='bold', color=color)

    ax.set_xlabel('Process: Lightweight  -->  Heavy', fontsize=12)
    ax.set_ylabel('Spec: Static  -->  Living', fontsize=12)
    ax.set_title('Figure 3: Positioning of Spec-Driven Development Tools',
                 fontsize=13, fontweight='bold')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_xticks([0, 0.25, 0.5, 0.75, 1.0])
    ax.set_yticks([0, 0.25, 0.5, 0.75, 1.0])
    ax.set_aspect('equal')

    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'tool_positioning.png'))
    plt.close()
    print('Generated: tool_positioning.png')


def fig4_phase_comparison():
    """図4: フェーズ別工数比較（AI有/無）"""
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
    ax.set_title('Figure 4: Phase-wise Effort Comparison (With/Without AI)', fontsize=13, fontweight='bold')
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


def fig5_test_ratio():
    """図5: テスト対コード比の業界比較"""
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
    ax.set_title('Figure 5: Test-to-Code Ratio - Industry Comparison', fontsize=13, fontweight='bold')
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


def fig6_maturity_progression():
    """図6: プロセス成熟度の変化（仕様量の推移）"""
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

    ax1.set_title('Figure 6: Process Maturity - Spec Volume vs Code Quality', fontsize=13, fontweight='bold')

    # Annotations
    ax1.annotate('Early: detailed exploration', xy=(0, 17868), xytext=(2, 16000),
                 arrowprops=dict(arrowstyle='->', color='gray'), fontsize=9, color='gray')
    ax1.annotate('Late: efficient routine', xy=(10, 809), xytext=(7, 4000),
                 arrowprops=dict(arrowstyle='->', color='gray'), fontsize=9, color='gray')

    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'maturity_progression.png'))
    plt.close()
    print('Generated: maturity_progression.png')


def fig9_cost_benefit():
    """図9: 人件費削減額 vs AI投資額の対比（標準シナリオ）"""
    labels = [
        'Without AI\n(estimated)',
        'With AI\n(human + AI cost)',
        'AI investment\n(standard scenario)'
    ]
    # 単位: 万円
    values = [9167, 2513, 13]
    colors = ['#d32f2f', '#1976d2', '#f9a825']

    fig, ax = plt.subplots(figsize=(10, 5))
    bars = ax.barh(labels, values, color=colors, alpha=0.85,
                   edgecolor='white', linewidth=1.5)

    ax.set_xlabel('Cost (10,000 JPY)', fontsize=12)
    ax.set_title('Figure 9: Human-Cost Reduction vs. AI Investment',
                 fontsize=13, fontweight='bold')
    ax.set_xlim(0, 10500)
    ax.invert_yaxis()

    # Value labels at the right end of each bar
    annotations = [
        ('91.67M JPY', '#d32f2f'),
        ('25.13M JPY (incl. 0.13M AI)', '#1976d2'),
        ('0.13M JPY', '#f9a825')
    ]
    for bar, (text, color) in zip(bars, annotations):
        ax.annotate(text,
                    xy=(bar.get_width(), bar.get_y() + bar.get_height() / 2),
                    xytext=(8, 0), textcoords='offset points',
                    va='center', fontsize=11, fontweight='bold', color=color)

    # Highlight reduction
    ax.annotate(
        'Human-cost reduction: 66.54M JPY\nAI investment ratio: 0.14% of human cost',
        xy=(5500, 2.4), xytext=(5500, 2.4),
        fontsize=10, color='#333',
        bbox=dict(boxstyle='round,pad=0.5',
                  facecolor='#fffde7', edgecolor='#f9a825', linewidth=1.2)
    )

    # Reference vertical line at the With-AI total
    ax.axvline(x=2513, color='#1976d2', linestyle='--',
               linewidth=0.8, alpha=0.5)

    ax.grid(axis='x', linestyle=':', alpha=0.4)

    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'cost_benefit.png'))
    plt.close()
    print('Generated: cost_benefit.png')


if __name__ == '__main__':
    fig3_tool_positioning()
    fig4_phase_comparison()
    fig5_test_ratio()
    fig6_maturity_progression()
    fig9_cost_benefit()
    print(f'\nAll figures saved to: {OUTPUT_DIR}')
