# Script to generate the ultra-luxury, highly-animated, pixel-faithful Clauze AI Frontend
import os

html_code = r'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Clauze AI — Brand Governance Platform</title>

<!-- High-Fashion Typography -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,300..800;1,9..144,300..800&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">

<style>
:root {
  /* Ultra-Luxury Obsidian & Champagne Palette */
  --sidebar-bg: #0d0e12;
  --sidebar-card: #151720;
  --sidebar-border: rgba(255, 255, 255, 0.07);
  --sidebar-text: #eae6df;
  --sidebar-muted: #8b8882;
  --sidebar-active-bg: linear-gradient(90deg, rgba(205, 164, 94, 0.16) 0%, rgba(205, 164, 94, 0.03) 100%);
  --sidebar-active-border: #cda45e;
  
  --gold-accent: #cda45e;
  --gold-light: #dfb76c;
  --gold-soft: rgba(205, 164, 94, 0.12);
  --gold-glow: 0 0 24px rgba(205, 164, 94, 0.25);

  --page-bg: #f8f6f0;
  --card-bg: #ffffff;
  --card-border: #ede8dc;
  --card-hover-border: #dfd8c7;
  
  --ink-primary: #121316;
  --ink-secondary: #565965;
  --ink-subtle: #8c8f9c;
  
  --status-green: #227a51;
  --status-green-bg: #ebf7f0;
  --status-green-border: #c2e5d1;
  
  --status-amber: #b86e00;
  --status-amber-bg: #fef5e7;
  --status-amber-border: #f9deb3;
  
  --status-red: #c0362c;
  --status-red-bg: #fdf0ef;
  --status-red-border: #f8cbca;

  --shadow-sm: 0 1px 3px rgba(18, 19, 22, 0.03), 0 1px 2px rgba(18, 19, 22, 0.02);
  --shadow-card: 0 4px 20px rgba(18, 19, 22, 0.04), 0 1px 3px rgba(18, 19, 22, 0.02);
  --shadow-hover: 0 12px 36px rgba(18, 19, 22, 0.08), 0 2px 6px rgba(18, 19, 22, 0.03);
  --shadow-modal: 0 24px 64px rgba(14, 15, 20, 0.22);
  
  --radius-lg: 16px;
  --radius-md: 12px;
  --radius-sm: 8px;
  --radius-pill: 9999px;
  
  --ease-spring: cubic-bezier(0.16, 1, 0.3, 1);
}

* { box-sizing: border-box; margin: 0; padding: 0; }
body {
  font-family: 'Plus Jakarta Sans', -apple-system, sans-serif;
  background-color: var(--page-bg);
  color: var(--ink-primary);
  line-height: 1.5;
  -webkit-font-smoothing: antialiased;
  overflow-x: hidden;
}

button, input, select, textarea { font-family: inherit; font-size: inherit; }
button { cursor: pointer; border: none; background: none; }

/* LAYOUT GRID */
.layout {
  display: grid;
  grid-template-columns: 260px minmax(0, 1fr);
  min-height: 100vh;
}

/* ==================== LEFT SIDEBAR ==================== */
.sidebar {
  background: var(--sidebar-bg);
  color: var(--sidebar-text);
  height: 100vh;
  position: sticky;
  top: 0;
  display: flex;
  flex-direction: column;
  border-right: 1px solid var(--sidebar-border);
  z-index: 40;
  user-select: none;
}

.brand-badge-area {
  padding: 24px 22px 20px;
  display: flex;
  align-items: center;
  gap: 12px;
}

.brand-icon-box {
  width: 36px;
  height: 36px;
  border-radius: 9px;
  background: linear-gradient(135deg, #d8ad63 0%, #aa7c30 100%);
  display: grid;
  place-items: center;
  color: #0d0e12;
  font-family: 'Fraunces', serif;
  font-weight: 800;
  font-size: 20px;
  box-shadow: 0 4px 12px rgba(205, 164, 94, 0.35);
  position: relative;
  overflow: hidden;
}
.brand-icon-box::after {
  content: '';
  position: absolute;
  top: -50%; left: -50%; width: 200%; height: 200%;
  background: linear-gradient(60deg, transparent, rgba(255,255,255,0.4), transparent);
  transform: rotate(30deg);
  animation: shine 4s infinite linear;
}
@keyframes shine {
  0% { transform: translateX(-100%) rotate(30deg); }
  20%, 100% { transform: translateX(100%) rotate(30deg); }
}

.brand-text { display: flex; flex-direction: column; }
.brand-title {
  font-family: 'Fraunces', serif;
  font-size: 19px;
  font-weight: 700;
  letter-spacing: -0.2px;
  color: #ffffff;
  line-height: 1.15;
}
.brand-sub {
  font-size: 9.5px;
  color: var(--gold-accent);
  text-transform: uppercase;
  letter-spacing: 1.4px;
  font-weight: 700;
  margin-top: 3px;
}

.sidebar-scroll {
  flex: 1;
  overflow-y: auto;
  padding: 10px 14px 20px;
  scrollbar-width: none;
}
.sidebar-scroll::-webkit-scrollbar { display: none; }

.nav-group-title {
  font-size: 10px;
  font-weight: 800;
  color: #63615b;
  text-transform: uppercase;
  letter-spacing: 1.2px;
  padding: 18px 12px 6px;
}

.nav-link {
  width: 100%;
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 9px 12px;
  border-radius: var(--radius-sm);
  color: var(--sidebar-muted);
  font-size: 13px;
  font-weight: 500;
  transition: all 0.2s var(--ease-spring);
  position: relative;
  text-align: left;
}
.nav-link:hover {
  color: #ffffff;
  background: rgba(255, 255, 255, 0.04);
  transform: translateX(2px);
}
.nav-link.active {
  color: #ffffff;
  background: var(--sidebar-active-bg);
  border: 1px solid rgba(205, 164, 94, 0.35);
  font-weight: 600;
  box-shadow: inset 0 0 14px rgba(205, 164, 94, 0.08);
}
.nav-link.active .nav-icon {
  color: var(--gold-accent);
  filter: drop-shadow(0 0 6px rgba(205, 164, 94, 0.5));
}
.nav-icon {
  width: 18px;
  height: 18px;
  color: #7b7871;
  transition: color 0.2s;
  display: grid;
  place-items: center;
}

.live-indicator {
  margin-left: auto;
  width: 7px;
  height: 7px;
  border-radius: 50%;
  background: #22c55e;
  box-shadow: 0 0 0 3px rgba(34, 197, 94, 0.25);
  animation: livePulse 2s infinite;
}
@keyframes livePulse {
  0%, 100% { transform: scale(1); opacity: 1; }
  50% { transform: scale(1.3); opacity: 0.6; }
}

.sidebar-footer {
  padding: 14px;
  border-top: 1px solid var(--sidebar-border);
  background: #090a0d;
}
.brand-pill-card {
  width: 100%;
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 8px 10px;
  border-radius: 10px;
  background: var(--sidebar-card);
  border: 1px solid rgba(255, 255, 255, 0.08);
  transition: all 0.2s;
  text-align: left;
}
.brand-pill-card:hover {
  border-color: rgba(205, 164, 94, 0.4);
  background: #1c1e29;
}
.leaf-badge {
  width: 26px;
  height: 26px;
  border-radius: 7px;
  background: rgba(205, 164, 94, 0.15);
  display: grid;
  place-items: center;
  color: var(--gold-accent);
}
.brand-pill-info { display: flex; flex-direction: column; flex: 1; }
.brand-pill-name { font-size: 12px; font-weight: 700; color: #fff; line-height: 1.2; }
.brand-pill-plan { font-size: 10px; color: #8b8882; }

/* ==================== TOP NAVIGATION ==================== */
.main-area {
  display: flex;
  flex-direction: column;
  min-width: 0;
}

.top-nav {
  height: 68px;
  background: rgba(248, 246, 240, 0.85);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  border-bottom: 1px solid var(--card-border);
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 36px;
  position: sticky;
  top: 0;
  z-index: 30;
}

.search-container {
  position: relative;
  width: 420px;
}
.search-input {
  width: 100%;
  height: 40px;
  background: #ffffff;
  border: 1px solid #e5dfd2;
  border-radius: var(--radius-sm);
  padding: 0 54px 0 38px;
  font-size: 13px;
  color: var(--ink-primary);
  outline: none;
  transition: all 0.2s;
  box-shadow: 0 1px 2px rgba(0,0,0,0.02);
}
.search-input:focus {
  border-color: var(--gold-accent);
  box-shadow: 0 0 0 3px rgba(205, 164, 94, 0.15);
}
.search-icon-left {
  position: absolute;
  left: 12px;
  top: 50%;
  transform: translateY(-50%);
  color: #9c978b;
}
.kbd-badge {
  position: absolute;
  right: 10px;
  top: 50%;
  transform: translateY(-50%);
  font-size: 10px;
  font-weight: 700;
  color: #8c887d;
  background: #f4eee3;
  padding: 3px 6px;
  border-radius: 4px;
  border: 1px solid #e4dccf;
}

.nav-actions {
  display: flex;
  align-items: center;
  gap: 18px;
}
.icon-btn {
  width: 38px;
  height: 38px;
  border-radius: var(--radius-sm);
  display: grid;
  place-items: center;
  color: #565965;
  transition: all 0.2s;
  position: relative;
}
.icon-btn:hover { background: #eee8dc; color: #121316; }
.unread-badge {
  position: absolute;
  top: 8px; right: 8px;
  width: 7px; height: 7px;
  border-radius: 50%;
  background: var(--status-red);
  box-shadow: 0 0 0 2px #ffffff;
}

.user-profile {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 4px 6px;
  border-radius: 30px;
  cursor: pointer;
  transition: background 0.15s;
}
.user-profile:hover { background: rgba(0,0,0,0.03); }
.user-avatar {
  width: 34px;
  height: 34px;
  border-radius: 50%;
  object-fit: cover;
  border: 1.5px solid var(--gold-accent);
}
.user-details { display: flex; flex-direction: column; }
.user-name { font-size: 13px; font-weight: 700; line-height: 1.2; }
.user-role { font-size: 11px; color: var(--ink-subtle); }

/* ==================== DASHBOARD CONTENT ==================== */
.content-body {
  padding: 32px 36px 48px;
  max-width: 1540px;
  margin: 0 auto;
  width: 100%;
}

.welcome-row {
  display: flex;
  align-items: flex-end;
  justify-content: space-between;
  margin-bottom: 28px;
  animation: fadeInDown 0.6s var(--ease-spring);
}
.headline-serif {
  font-family: 'Fraunces', serif;
  font-size: 33px;
  font-weight: 700;
  letter-spacing: -0.5px;
  color: var(--ink-primary);
  line-height: 1.2;
}
.headline-sub {
  font-size: 14px;
  color: var(--ink-secondary);
  margin-top: 4px;
}
.date-selector-pill {
  display: flex;
  align-items: center;
  gap: 14px;
  font-size: 13px;
  font-weight: 600;
  color: var(--ink-secondary);
}
.dropdown-trigger {
  background: #ffffff;
  border: 1px solid var(--card-border);
  padding: 7px 14px;
  border-radius: var(--radius-sm);
  display: inline-flex;
  align-items: center;
  gap: 8px;
  font-size: 13px;
  font-weight: 600;
  color: var(--ink-primary);
  box-shadow: var(--shadow-sm);
  transition: all 0.2s;
}
.dropdown-trigger:hover {
  border-color: var(--gold-accent);
  box-shadow: var(--shadow-card);
}

/* ==================== 4 KPI CARDS ==================== */
.kpi-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 18px;
  margin-bottom: 28px;
}
.kpi-card {
  background: var(--card-bg);
  border: 1px solid var(--card-border);
  border-radius: var(--radius-md);
  padding: 20px 22px;
  box-shadow: var(--shadow-card);
  display: flex;
  flex-direction: column;
  position: relative;
  overflow: hidden;
  transition: transform 0.25s var(--ease-spring), box-shadow 0.25s, border-color 0.25s;
  animation: scaleIn 0.5s var(--ease-spring) both;
}
.kpi-card:hover {
  transform: translateY(-3px);
  box-shadow: var(--shadow-hover);
  border-color: var(--card-hover-border);
}
.kpi-card::before {
  content: '';
  position: absolute;
  top: 0; left: 0; right: 0; height: 3px;
  background: transparent;
  transition: background 0.3s;
}
.kpi-card:hover::before {
  background: linear-gradient(90deg, var(--gold-accent), transparent);
}

.kpi-top-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 12px;
}
.kpi-label {
  font-size: 13px;
  font-weight: 600;
  color: var(--ink-secondary);
}
.kpi-icon-box {
  width: 34px;
  height: 34px;
  border-radius: 8px;
  display: grid;
  place-items: center;
  font-size: 16px;
}
.kpi-icon-warm { background: #faf4e6; color: #b68735; }
.kpi-icon-red { background: #fdf0ef; color: #c0362c; }
.kpi-icon-green { background: #ecf7f1; color: #227a51; }
.kpi-icon-gold { background: #fdf6ea; color: #c38c2f; }

.kpi-bottom-row {
  display: flex;
  align-items: flex-end;
  justify-content: space-between;
}
.kpi-val {
  font-size: 32px;
  font-weight: 800;
  letter-spacing: -1px;
  line-height: 1;
  color: var(--ink-primary);
}
.kpi-delta {
  display: flex;
  align-items: center;
  gap: 5px;
  font-size: 11.5px;
  font-weight: 700;
  margin-top: 8px;
}
.delta-green { color: var(--status-green); }
.delta-red { color: var(--status-red); }
.delta-sub { color: var(--ink-subtle); font-weight: 500; font-size: 11px; margin-left: 2px; }

/* MINI SPARKLINES (SVG BAR CLUSTERS) */
.mini-spark {
  display: flex;
  align-items: flex-end;
  gap: 3px;
  height: 28px;
  padding-bottom: 2px;
}
.spark-bar {
  width: 4px;
  border-radius: 2px;
  transition: height 0.5s ease;
}

/* ==================== MAIN 2-COLUMN SECTION ==================== */
.middle-grid {
  display: grid;
  grid-template-columns: minmax(0, 1.75fr) minmax(360px, 1fr);
  gap: 24px;
  margin-bottom: 28px;
}

.luxury-card {
  background: var(--card-bg);
  border: 1px solid var(--card-border);
  border-radius: var(--radius-lg);
  padding: 24px;
  box-shadow: var(--shadow-card);
  display: flex;
  flex-direction: column;
}

.card-title-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 20px;
}
.card-header-left {
  display: flex;
  align-items: center;
  gap: 12px;
}
.section-icon {
  width: 32px;
  height: 32px;
  border-radius: 8px;
  background: #fbf5ea;
  color: var(--gold-accent);
  display: grid;
  place-items: center;
}
.card-headline {
  font-size: 16px;
  font-weight: 700;
  letter-spacing: -0.2px;
}
.card-caption {
  font-size: 12px;
  color: var(--ink-subtle);
  margin-top: 2px;
}

.btn-luxury-dark {
  background: #17181f;
  color: #ffffff;
  padding: 8px 16px;
  border-radius: var(--radius-sm);
  font-size: 12.5px;
  font-weight: 700;
  display: inline-flex;
  align-items: center;
  gap: 8px;
  transition: all 0.2s var(--ease-spring);
  border: 1px solid rgba(255,255,255,0.08);
}
.btn-luxury-dark:hover {
  background: #252733;
  transform: translateY(-1px);
  box-shadow: 0 4px 14px rgba(0,0,0,0.15);
}

/* RECENT REVIEWS TABLE */
.review-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 13px;
}
.review-table th {
  text-align: left;
  font-size: 10.5px;
  font-weight: 800;
  color: #8c8f9c;
  text-transform: uppercase;
  letter-spacing: 0.8px;
  padding: 10px 12px;
  border-bottom: 1px solid #f0ebe0;
}
.review-table td {
  padding: 13px 12px;
  border-bottom: 1px solid #f6f2e9;
  vertical-align: middle;
}
.review-row {
  cursor: pointer;
  transition: background 0.15s;
}
.review-row:hover {
  background: #fcfbf8;
}

.content-cell {
  display: flex;
  align-items: center;
  gap: 12px;
}
.thumb-box {
  width: 40px;
  height: 40px;
  border-radius: 8px;
  overflow: hidden;
  background: #eee8dc;
  flex-shrink: 0;
  box-shadow: 0 1px 3px rgba(0,0,0,0.08);
}
.thumb-box img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}
.content-text { display: flex; flex-direction: column; }
.content-title { font-weight: 700; font-size: 13.5px; color: var(--ink-primary); line-height: 1.25; }
.content-meta { font-size: 11.5px; color: var(--ink-subtle); margin-top: 2px; }

.channel-tag {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  font-size: 12px;
  color: var(--ink-secondary);
  font-weight: 600;
}

.status-pill {
  display: inline-flex;
  align-items: center;
  gap: 5px;
  padding: 4px 10px;
  border-radius: var(--radius-pill);
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.2px;
}
.pill-needs-review { background: #fdf0ef; color: #c0362c; border: 1px solid #fad5d3; }
.pill-in-review { background: #fef5e7; color: #b86e00; border: 1px solid #fbe5c5; }
.pill-compliant { background: #ebf7f0; color: #227a51; border: 1px solid #c9ecda; }
.pill-high-risk { background: #dc2626; color: #ffffff; box-shadow: 0 2px 6px rgba(220, 38, 38, 0.35); }

.more-action-btn {
  color: #9c978b;
  font-size: 16px;
  padding: 4px 8px;
  border-radius: 4px;
}
.more-action-btn:hover { background: #eee8dc; color: #121316; }

/* ==================== RIGHT COLUMN (DONUT & TOP ISSUES) ==================== */
.right-col {
  display: flex;
  flex-direction: column;
  gap: 24px;
}

.donut-layout {
  display: flex;
  align-items: center;
  gap: 22px;
  padding: 6px 0;
}
.donut-svg-wrapper {
  position: relative;
  width: 140px;
  height: 140px;
  flex-shrink: 0;
}
.donut-center-text {
  position: absolute;
  inset: 0;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  pointer-events: none;
}
.donut-center-num {
  font-size: 24px;
  font-weight: 800;
  letter-spacing: -0.5px;
  line-height: 1;
}
.donut-center-lbl {
  font-size: 11px;
  color: var(--ink-subtle);
  margin-top: 2px;
}

.donut-legend {
  display: flex;
  flex-direction: column;
  gap: 8px;
  flex: 1;
}
.legend-item {
  display: flex;
  align-items: center;
  justify-content: space-between;
  font-size: 12.5px;
}
.legend-left { display: flex; align-items: center; gap: 8px; }
.legend-dot { width: 8px; height: 8px; border-radius: 50%; }
.legend-label { color: var(--ink-secondary); font-weight: 500; }
.legend-val { font-weight: 700; color: var(--ink-primary); }
.legend-pct { color: var(--ink-subtle); font-size: 11px; font-weight: 500; margin-left: 4px; }

/* TOP ISSUES PROGRESS BARS */
.issues-list {
  display: flex;
  flex-direction: column;
  gap: 13px;
}
.issue-row {
  display: grid;
  grid-template-columns: minmax(0, 1.4fr) 30px minmax(90px, 1fr);
  align-items: center;
  gap: 12px;
  font-size: 12.5px;
}
.issue-name {
  color: var(--ink-secondary);
  font-weight: 600;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
.issue-count {
  font-weight: 800;
  text-align: right;
  color: var(--ink-primary);
}
.issue-bar-track {
  height: 8px;
  background: #f4eee2;
  border-radius: 4px;
  overflow: hidden;
  position: relative;
}
.issue-bar-fill {
  height: 100%;
  border-radius: 4px;
  transition: width 1s var(--ease-spring);
}

/* ==================== BOTTOM FULL-WIDTH TRENDS ==================== */
.trend-legend-row {
  display: flex;
  align-items: center;
  gap: 20px;
  font-size: 12px;
  font-weight: 600;
  color: var(--ink-secondary);
}
.legend-pill-tag {
  display: flex;
  align-items: center;
  gap: 6px;
}
.legend-diamond { width: 8px; height: 8px; transform: rotate(45deg); }

.chart-wrapper {
  margin-top: 14px;
  position: relative;
  height: 160px;
  width: 100%;
}

/* SUB-PAGES MODES */
.tab-page {
  display: none;
}
.tab-page.active {
  display: block;
  animation: fadeIn 0.4s var(--ease-spring);
}
@keyframes fadeIn {
  from { opacity: 0; transform: translateY(6px); }
  to { opacity: 1; transform: translateY(0); }
}
@keyframes fadeInDown {
  from { opacity: 0; transform: translateY(-10px); }
  to { opacity: 1; transform: translateY(0); }
}
@keyframes scaleIn {
  from { opacity: 0; transform: scale(0.97); }
  to { opacity: 1; transform: scale(1); }
}

/* SLIDING DRAWER INSPECTOR */
.drawer-backdrop {
  position: fixed;
  inset: 0;
  background: rgba(13, 14, 18, 0.45);
  backdrop-filter: blur(4px);
  z-index: 90;
  opacity: 0;
  pointer-events: none;
  transition: opacity 0.3s;
}
.drawer-backdrop.open {
  opacity: 1;
  pointer-events: auto;
}
.drawer-panel {
  position: fixed;
  top: 0; right: 0; bottom: 0;
  width: 580px;
  max-width: 90vw;
  background: #ffffff;
  box-shadow: var(--shadow-modal);
  z-index: 100;
  transform: translateX(100%);
  transition: transform 0.4s var(--ease-spring);
  display: flex;
  flex-direction: column;
}
.drawer-backdrop.open .drawer-panel {
  transform: translateX(0);
}

.drawer-header {
  padding: 24px 28px;
  border-bottom: 1px solid var(--card-border);
  display: flex;
  align-items: center;
  justify-content: space-between;
}
.drawer-body {
  padding: 28px;
  overflow-y: auto;
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 20px;
}
</style>
</head>
<body>

<div class="layout">
  
  <!-- ==================== SIDEBAR ==================== -->
  <aside class="sidebar">
    <div class="brand-badge-area">
      <div class="brand-icon-box">C</div>
      <div class="brand-text">
        <span class="brand-title">Clauze AI</span>
        <span class="brand-sub">Brand Governance</span>
      </div>
    </div>

    <div class="sidebar-scroll">
      <!-- MAIN -->
      <div class="nav-group-title">Main</div>
      <button class="nav-link active" onclick="switchNav('dashboard', this)">
        <span class="nav-icon"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></svg></span>
        <span>Dashboard</span>
      </button>

      <button class="nav-link" onclick="switchNav('review', this)">
        <span class="nav-icon"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/></svg></span>
        <span>Content Review</span>
      </button>

      <button class="nav-link" onclick="switchNav('creative', this)">
        <span class="nav-icon"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2"/><circle cx="8.5" cy="8.5" r="1.5"/><polyline points="21 15 16 10 5 21"/></svg></span>
        <span>Creative Audit</span>
      </button>

      <button class="nav-link" onclick="switchNav('approval', this)">
        <span class="nav-icon"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><ellipse cx="12" cy="5" rx="9" ry="3"/><path d="M21 12c0 1.66-4 3-9 3s-9-1.34-9-3"/><path d="M3 5v14c0 1.66 4 3 9 3s9-1.34 9-3V5"/></svg></span>
        <span>Approval Queue</span>
      </button>

      <button class="nav-link" onclick="switchNav('insights', this)">
        <span class="nav-icon"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="20" x2="18" y2="10"/><line x1="12" y1="20" x2="12" y2="4"/><line x1="6" y1="20" x2="6" y2="14"/></svg></span>
        <span>Insights</span>
      </button>

      <!-- KNOWLEDGE -->
      <div class="nav-group-title">Knowledge</div>
      <button class="nav-link" onclick="switchNav('brandkit', this)">
        <span class="nav-icon"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"/></svg></span>
        <span>Brand Kit</span>
      </button>

      <button class="nav-link" onclick="switchNav('regulations', this)">
        <span class="nav-icon"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg></span>
        <span>Regulations</span>
      </button>

      <button class="nav-link" onclick="switchNav('claims', this)">
        <span class="nav-icon"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="12 2 2 7 12 12 22 7 12 2"/><polyline points="2 17 12 22 22 17"/><polyline points="2 12 12 17 22 12"/></svg></span>
        <span>Claims Library</span>
      </button>

      <button class="nav-link" onclick="switchNav('templates', this)">
        <span class="nav-icon"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="8" y1="6" x2="21" y2="6"/><line x1="8" y1="12" x2="21" y2="12"/><line x1="8" y1="18" x2="21" y2="18"/><line x1="3" y1="6" x2="3.01" y2="6"/><line x1="3" y1="12" x2="3.01" y2="12"/><line x1="3" y1="18" x2="3.01" y2="18"/></svg></span>
        <span>Templates</span>
      </button>

      <!-- ADVANCED -->
      <div class="nav-group-title">Advanced</div>
      <button class="nav-link" onclick="switchNav('interceptor', this)">
        <span class="nav-icon"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="6"/><circle cx="12" cy="12" r="2"/></svg></span>
        <span>Live Interceptor</span>
        <span class="live-indicator"></span>
      </button>

      <button class="nav-link" onclick="switchNav('adversarial', this)">
        <span class="nav-icon"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M10 2v7.31L4.62 17A2 2 0 0 0 6.27 20h11.46a2 2 0 0 0 1.65-3L14 9.31V2"/></svg></span>
        <span>Adversarial Test</span>
      </button>

      <button class="nav-link" onclick="switchNav('auditlogs', this)">
        <span class="nav-icon"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg></span>
        <span>Audit Logs</span>
      </button>

      <!-- SETTINGS -->
      <div class="nav-group-title">Settings</div>
      <button class="nav-link" onclick="switchNav('workspace', this)">
        <span class="nav-icon"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1 0 2.83 2 2 0 0 1-2.83 0l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-2 2 2 2 0 0 1-2-2v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83 0 2 2 0 0 1 0-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1-2-2 2 2 0 0 1 2-2h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 0-2.83 2 2 0 0 1 2.83 0l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 2-2 2 2 0 0 1 2 2v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 0 2 2 0 0 1 0 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 2 2 2 2 0 0 1-2 2h-.09a1.65 1.65 0 0 0-1.51 1z"/></svg></span>
        <span>Workspace</span>
      </button>

      <button class="nav-link" onclick="switchNav('integrations', this)">
        <span class="nav-icon"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"/><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"/></svg></span>
        <span>Integrations</span>
      </button>

      <button class="nav-link" onclick="switchNav('team', this)">
        <span class="nav-icon"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg></span>
        <span>Team & Access</span>
      </button>
    </div>

    <!-- BOTTOM BRAND CARD -->
    <div class="sidebar-footer">
      <button class="brand-pill-card" onclick="openBrandModal()">
        <div class="leaf-badge">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor"><path d="M17 8C8 10 5.9 16.17 3.82 21.34L5.71 22l1-2.3A4.49 4.49 0 0 0 8 20C19 20 22 3 22 3c-1 2-8 2.25-13 3.25S2 11.5 2 13.5s1.75 3.75 1.75 3.75C7 8 17 8 17 8z"/></svg>
        </div>
        <div class="brand-pill-info">
          <span class="brand-pill-name" id="sidebarBrandName">Northstar Skincare</span>
          <span class="brand-pill-plan">Enterprise Plan</span>
        </div>
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#717482" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
      </button>
    </div>
  </aside>

  <!-- ==================== MAIN WORKSPACE ==================== -->
  <main class="main-area">
    <!-- TOP NAV -->
    <header class="top-nav">
      <div class="search-container">
        <svg class="search-icon-left" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
        <input type="text" class="search-input" placeholder="Search assets, claims, guidelines..." onfocus="this.select()">
        <span class="kbd-badge">Ctrl K</span>
      </div>

      <div class="nav-actions">
        <button class="icon-btn" title="Notifications" onclick="alert('All compliance systems normal. 0 active alerts.')">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 8A6 6 0 0 0 6 8c0 7-3 9-3 9h18s-3-2-3-9"/><path d="M13.73 21a2 2 0 0 1-3.46 0"/></svg>
          <span class="unread-badge"></span>
        </button>

        <div class="user-profile" onclick="switchNav('workspace', null)">
          <img src="https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=100&auto=format&fit=crop&q=80" alt="Atharv" class="user-avatar">
          <div class="user-details">
            <span class="user-name">Atharv</span>
            <span class="user-role">Admin</span>
          </div>
        </div>
      </div>
    </header>

    <!-- ==================== PAGE VIEW: DASHBOARD ==================== -->
    <div class="content-body tab-page active" id="view-dashboard">
      <!-- WELCOME ROW -->
      <div class="welcome-row">
        <div>
          <h1 class="headline-serif">Good morning, Atharv.</h1>
          <p class="headline-sub">Your brand content is protected and ready to go live.</p>
        </div>
        <div class="date-selector-pill">
          <span>Fri, 24 Oct 2026</span>
          <button class="dropdown-trigger">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="4" width="18" height="18" rx="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg>
            <span>Last 7 days</span>
            <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
          </button>
        </div>
      </div>

      <!-- 4 KPI CARDS -->
      <div class="kpi-grid">
        <!-- 1. Assets Reviewed -->
        <div class="kpi-card">
          <div class="kpi-top-row">
            <span class="kpi-label">Assets Reviewed</span>
            <div class="kpi-icon-box kpi-icon-warm">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/></svg>
            </div>
          </div>
          <div class="kpi-bottom-row">
            <div>
              <div class="kpi-val counter" data-target="128">128</div>
              <div class="kpi-delta delta-green">
                <span>↑ 18%</span>
                <span class="delta-sub">vs last week</span>
              </div>
            </div>
            <!-- Mini sparkline -->
            <div class="mini-spark">
              <div class="spark-bar" style="height: 12px; background: #e8dcc4;"></div>
              <div class="spark-bar" style="height: 16px; background: #dfceb0;"></div>
              <div class="spark-bar" style="height: 10px; background: #e8dcc4;"></div>
              <div class="spark-bar" style="height: 20px; background: #dfceb0;"></div>
              <div class="spark-bar" style="height: 14px; background: #e8dcc4;"></div>
              <div class="spark-bar" style="height: 26px; background: #cda45e;"></div>
            </div>
          </div>
        </div>

        <!-- 2. Policy Violations -->
        <div class="kpi-card">
          <div class="kpi-top-row">
            <span class="kpi-label">Policy Violations</span>
            <div class="kpi-icon-box kpi-icon-red">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"/><line x1="12" y1="9" x2="12" y2="13"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg>
            </div>
          </div>
          <div class="kpi-bottom-row">
            <div>
              <div class="kpi-val counter" data-target="4">4</div>
              <div class="kpi-delta delta-green">
                <span>↓ 60%</span>
                <span class="delta-sub">vs last week</span>
              </div>
            </div>
            <div class="mini-spark">
              <div class="spark-bar" style="height: 24px; background: #fad1cf;"></div>
              <div class="spark-bar" style="height: 20px; background: #fad1cf;"></div>
              <div class="spark-bar" style="height: 16px; background: #fad1cf;"></div>
              <div class="spark-bar" style="height: 12px; background: #fad1cf;"></div>
              <div class="spark-bar" style="height: 15px; background: #fad1cf;"></div>
              <div class="spark-bar" style="height: 8px; background: #c0362c;"></div>
            </div>
          </div>
        </div>

        <!-- 3. Publish Ready -->
        <div class="kpi-card">
          <div class="kpi-top-row">
            <span class="kpi-label">Publish Ready</span>
            <div class="kpi-icon-box kpi-icon-green">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><polyline points="9 12 11 14 15 10"/></svg>
            </div>
          </div>
          <div class="kpi-bottom-row">
            <div>
              <div class="kpi-val"><span class="counter" data-target="92">92</span>%</div>
              <div class="kpi-delta delta-green">
                <span>↑ 6%</span>
                <span class="delta-sub">vs last week</span>
              </div>
            </div>
            <div class="mini-spark">
              <div class="spark-bar" style="height: 18px; background: #c6ebd7;"></div>
              <div class="spark-bar" style="height: 19px; background: #c6ebd7;"></div>
              <div class="spark-bar" style="height: 22px; background: #c6ebd7;"></div>
              <div class="spark-bar" style="height: 21px; background: #c6ebd7;"></div>
              <div class="spark-bar" style="height: 24px; background: #c6ebd7;"></div>
              <div class="spark-bar" style="height: 28px; background: #227a51;"></div>
            </div>
          </div>
        </div>

        <!-- 4. Pending Approvals -->
        <div class="kpi-card">
          <div class="kpi-top-row">
            <span class="kpi-label">Pending Approvals</span>
            <div class="kpi-icon-box kpi-icon-gold">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>
            </div>
          </div>
          <div class="kpi-bottom-row">
            <div>
              <div class="kpi-val counter" data-target="3">3</div>
              <div class="kpi-delta delta-red">
                <span>↑ 2 new</span>
                <span class="delta-sub">since yesterday</span>
              </div>
            </div>
            <div class="mini-spark">
              <div class="spark-bar" style="height: 8px; background: #edd9b4;"></div>
              <div class="spark-bar" style="height: 10px; background: #edd9b4;"></div>
              <div class="spark-bar" style="height: 12px; background: #edd9b4;"></div>
              <div class="spark-bar" style="height: 8px; background: #edd9b4;"></div>
              <div class="spark-bar" style="height: 14px; background: #edd9b4;"></div>
              <div class="spark-bar" style="height: 20px; background: #c38c2f;"></div>
            </div>
          </div>
        </div>
      </div>

      <!-- MIDDLE 2-COLUMN SECTION -->
      <div class="middle-grid">
        
        <!-- LEFT: RECENT REVIEWS TABLE -->
        <div class="luxury-card">
          <div class="card-title-row">
            <div class="card-header-left">
              <div class="section-icon">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/></svg>
              </div>
              <div>
                <h3 class="card-headline">Recent Reviews</h3>
                <p class="card-caption">Latest content checked by Clauze AI</p>
              </div>
            </div>
            <button class="btn-luxury-dark" onclick="openReviewModal()">
              <span>+ New Review</span>
            </button>
          </div>

          <table class="review-table">
            <thead>
              <tr>
                <th>Content</th>
                <th>Channel</th>
                <th>Status</th>
                <th>Violations</th>
                <th>Reviewed</th>
                <th style="text-align:right;">···</th>
              </tr>
            </thead>
            <tbody>
              <!-- Row 1 -->
              <tr class="review-row" onclick="inspectRow('Summer Serum Campaign', 'Needs Review', 2, 'Hero banner • Northstar Skincare')">
                <td>
                  <div class="content-cell">
                    <div class="thumb-box">
                      <img src="https://images.unsplash.com/photo-1620916566398-39f1143ab7be?w=80&auto=format&fit=crop&q=80" alt="Serum">
                    </div>
                    <div class="content-text">
                      <span class="content-title">Summer Serum Campaign</span>
                      <span class="content-meta">Hero banner • Northstar Skincare</span>
                    </div>
                  </div>
                </td>
                <td>
                  <div class="channel-tag">
                    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="2" width="20" height="20" rx="5"/><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"/><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"/></svg>
                    <span>Instagram</span>
                  </div>
                </td>
                <td><span class="status-pill pill-needs-review">Needs Review</span></td>
                <td><strong style="color:var(--status-red); font-size:13.5px;">2</strong></td>
                <td style="color:var(--ink-subtle);">8 min ago</td>
                <td style="text-align:right;"><span class="more-action-btn">···</span></td>
              </tr>

              <!-- Row 2 -->
              <tr class="review-row" onclick="inspectRow('Landing Page Copy', 'In Review', 1, 'Product description • Northstar')">
                <td>
                  <div class="content-cell">
                    <div class="thumb-box">
                      <img src="https://images.unsplash.com/photo-1556228720-195a672e8a03?w=80&auto=format&fit=crop&q=80" alt="Cream">
                    </div>
                    <div class="content-text">
                      <span class="content-title">Landing Page Copy</span>
                      <span class="content-meta">Product description</span>
                    </div>
                  </div>
                </td>
                <td>
                  <div class="channel-tag">
                    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg>
                    <span>Web</span>
                  </div>
                </td>
                <td><span class="status-pill pill-in-review">In Review</span></td>
                <td><strong style="color:var(--status-amber); font-size:13.5px;">1</strong></td>
                <td style="color:var(--ink-subtle);">24 min ago</td>
                <td style="text-align:right;"><span class="more-action-btn">···</span></td>
              </tr>

              <!-- Row 3 -->
              <tr class="review-row" onclick="inspectRow('Hydration Routine Ad', 'Compliant', 0, 'Paid social variant')">
                <td>
                  <div class="content-cell">
                    <div class="thumb-box">
                      <img src="https://images.unsplash.com/photo-1570172619644-dfd03ed5d881?w=80&auto=format&fit=crop&q=80" alt="Routine">
                    </div>
                    <div class="content-text">
                      <span class="content-title">Hydration Routine Ad</span>
                      <span class="content-meta">Paid social variant</span>
                    </div>
                  </div>
                </td>
                <td>
                  <div class="channel-tag">
                    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg>
                    <span>Paid Social</span>
                  </div>
                </td>
                <td><span class="status-pill pill-compliant">Compliant</span></td>
                <td><strong style="color:var(--status-green); font-size:13.5px;">0</strong></td>
                <td style="color:var(--ink-subtle);">1 hr ago</td>
                <td style="text-align:right;"><span class="more-action-btn">···</span></td>
              </tr>

              <!-- Row 4 -->
              <tr class="review-row" onclick="inspectRow('Influencer Post', 'High Risk', 3, 'Instagram caption')">
                <td>
                  <div class="content-cell">
                    <div class="thumb-box">
                      <img src="https://images.unsplash.com/photo-1598440947619-2c35fc9aa908?w=80&auto=format&fit=crop&q=80" alt="Cosmetic">
                    </div>
                    <div class="content-text">
                      <span class="content-title">Influencer Post</span>
                      <span class="content-meta">Instagram caption</span>
                    </div>
                  </div>
                </td>
                <td>
                  <div class="channel-tag">
                    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="2" width="20" height="20" rx="5"/><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"/></svg>
                    <span>Instagram</span>
                  </div>
                </td>
                <td><span class="status-pill pill-high-risk">High Risk</span></td>
                <td><strong style="color:var(--status-red); font-size:13.5px;">3</strong></td>
                <td style="color:var(--ink-subtle);">2 hr ago</td>
                <td style="text-align:right;"><span class="more-action-btn">···</span></td>
              </tr>

              <!-- Row 5 -->
              <tr class="review-row" onclick="inspectRow('Ingredient Claim Text', 'Compliant', 0, 'Benefit statement')">
                <td>
                  <div class="content-cell">
                    <div class="thumb-box">
                      <img src="https://images.unsplash.com/photo-1518531933037-91b2f5f229cc?w=80&auto=format&fit=crop&q=80" alt="Botanical">
                    </div>
                    <div class="content-text">
                      <span class="content-title">Ingredient Claim Text</span>
                      <span class="content-meta">Benefit statement</span>
                    </div>
                  </div>
                </td>
                <td>
                  <div class="channel-tag">
                    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/></svg>
                    <span>Web</span>
                  </div>
                </td>
                <td><span class="status-pill pill-compliant">Compliant</span></td>
                <td><strong style="color:var(--status-green); font-size:13.5px;">0</strong></td>
                <td style="color:var(--ink-subtle);">3 hr ago</td>
                <td style="text-align:right;"><span class="more-action-btn">···</span></td>
              </tr>
            </tbody>
          </table>
        </div>

        <!-- RIGHT: RISK DISTRIBUTION & TOP ISSUES -->
        <div class="right-col">
          
          <!-- RISK DISTRIBUTION -->
          <div class="luxury-card">
            <div class="card-title-row">
              <div class="card-header-left">
                <div class="section-icon">
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 3v18"/><path d="M3 6l9-3 9 3"/><path d="M3 18l9 3 9-3"/><circle cx="12" cy="12" r="2"/></svg>
                </div>
                <h3 class="card-headline">Risk Distribution</h3>
              </div>
              <button class="dropdown-trigger" style="font-size:11.5px; padding:4px 10px;">
                <span>Last 7 days</span>
                <svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
              </button>
            </div>

            <div class="donut-layout">
              <div class="donut-svg-wrapper">
                <svg width="140" height="140" viewBox="0 0 140 140" style="transform: rotate(-90deg);">
                  <!-- Circle segments: 71.9% Green, 14.1% Teal, 8.6% Amber, 5.5% Red -->
                  <!-- Circumference = 2 * PI * 52 = 326.7 -->
                  <circle cx="70" cy="70" r="52" fill="none" stroke="#f0ece2" stroke-width="15"/>
                  <!-- Green (Compliant: 71.9% = 234.9) -->
                  <circle cx="70" cy="70" r="52" fill="none" stroke="#227a51" stroke-width="15" stroke-dasharray="234.9 326.7" stroke-dashoffset="0" style="transition: stroke-dasharray 1s ease;"/>
                  <!-- Teal/Light Green (Low: 14.1% = 46.0) -->
                  <circle cx="70" cy="70" r="52" fill="none" stroke="#5cb88a" stroke-width="15" stroke-dasharray="46.0 326.7" stroke-dashoffset="-234.9"/>
                  <!-- Amber (Medium: 8.6% = 28.1) -->
                  <circle cx="70" cy="70" r="52" fill="none" stroke="#df9b3b" stroke-width="15" stroke-dasharray="28.1 326.7" stroke-dashoffset="-280.9"/>
                  <!-- Red (High: 5.5% = 17.9) -->
                  <circle cx="70" cy="70" r="52" fill="none" stroke="#dc2626" stroke-width="15" stroke-dasharray="17.9 326.7" stroke-dashoffset="-309.0"/>
                </svg>
                <div class="donut-center-text">
                  <span class="donut-center-num">128</span>
                  <span class="donut-center-lbl">assets</span>
                </div>
              </div>

              <div class="donut-legend">
                <div class="legend-item">
                  <div class="legend-left">
                    <span class="legend-dot" style="background:#227a51;"></span>
                    <span class="legend-label">Compliant</span>
                  </div>
                  <div>
                    <span class="legend-val">92</span>
                    <span class="legend-pct">(71.9%)</span>
                  </div>
                </div>

                <div class="legend-item">
                  <div class="legend-left">
                    <span class="legend-dot" style="background:#5cb88a;"></span>
                    <span class="legend-label">Low Risk</span>
                  </div>
                  <div>
                    <span class="legend-val">18</span>
                    <span class="legend-pct">(14.1%)</span>
                  </div>
                </div>

                <div class="legend-item">
                  <div class="legend-left">
                    <span class="legend-dot" style="background:#df9b3b;"></span>
                    <span class="legend-label">Medium Risk</span>
                  </div>
                  <div>
                    <span class="legend-val">11</span>
                    <span class="legend-pct">(8.6%)</span>
                  </div>
                </div>

                <div class="legend-item">
                  <div class="legend-left">
                    <span class="legend-dot" style="background:#dc2626;"></span>
                    <span class="legend-label">High Risk</span>
                  </div>
                  <div>
                    <span class="legend-val">7</span>
                    <span class="legend-pct">(5.5%)</span>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- TOP ISSUES -->
          <div class="luxury-card">
            <div class="card-title-row">
              <div class="card-header-left">
                <div class="section-icon">
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
                </div>
                <h3 class="card-headline">Top Issues</h3>
              </div>
              <a href="javascript:void(0)" onclick="switchNav('regulations', null)" style="font-size:12px; color:var(--gold-accent); font-weight:700; text-decoration:none;">View all</a>
            </div>

            <div class="issues-list">
              <!-- Issue 1 -->
              <div class="issue-row">
                <span class="issue-name" title="Medical efficacy claims">Medical efficacy claims</span>
                <span class="issue-count">24</span>
                <div class="issue-bar-track">
                  <div class="issue-bar-fill" style="width: 85%; background: #dc2626;"></div>
                </div>
              </div>

              <!-- Issue 2 -->
              <div class="issue-row">
                <span class="issue-name" title="Unsupported product claims">Unsupported product claims</span>
                <span class="issue-count">18</span>
                <div class="issue-bar-track">
                  <div class="issue-bar-fill" style="width: 65%; background: #e07a30;"></div>
                </div>
              </div>

              <!-- Issue 3 -->
              <div class="issue-row">
                <span class="issue-name" title="Disclaimer & transparency">Disclaimer & transparency</span>
                <span class="issue-count">12</span>
                <div class="issue-bar-track">
                  <div class="issue-bar-fill" style="width: 44%; background: #dfa030;"></div>
                </div>
              </div>

              <!-- Issue 4 -->
              <div class="issue-row">
                <span class="issue-name" title="Brand voice misalignment">Brand voice misalignment</span>
                <span class="issue-count">9</span>
                <div class="issue-bar-track">
                  <div class="issue-bar-fill" style="width: 32%; background: #dfc18b;"></div>
                </div>
              </div>

              <!-- Issue 5 -->
              <div class="issue-row">
                <span class="issue-name" title="Off-brand color usage">Off-brand color usage</span>
                <span class="issue-count">6</span>
                <div class="issue-bar-track">
                  <div class="issue-bar-fill" style="width: 22%; background: #ebdcb9;"></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- BOTTOM FULL-WIDTH: REVIEW TRENDS -->
      <div class="luxury-card">
        <div class="card-title-row">
          <div class="card-header-left">
            <div class="section-icon">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/></svg>
            </div>
            <div>
              <h3 class="card-headline">Review Trends</h3>
              <p class="card-caption">Number of assets reviewed and violation rate</p>
            </div>
          </div>

          <div style="display:flex; align-items:center; gap:24px;">
            <div class="trend-legend-row">
              <div class="legend-pill-tag">
                <span class="legend-diamond" style="background:#dfb76c;"></span>
                <span>Assets Reviewed</span>
              </div>
              <div class="legend-pill-tag">
                <span class="legend-diamond" style="background:#c0362c;"></span>
                <span>Violation Rate</span>
              </div>
            </div>

            <button class="dropdown-trigger" style="font-size:11.5px; padding:4px 10px;">
              <span>Last 14 days</span>
              <svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
            </button>
          </div>
        </div>

        <!-- DUAL AXIS TREND CHART (SVG) -->
        <div class="chart-wrapper">
          <svg width="100%" height="160" viewBox="0 0 1000 160" preserveAspectRatio="none">
            <!-- Grid lines -->
            <line x1="40" y1="20" x2="980" y2="20" stroke="#f0ebe0" stroke-dasharray="3 3"/>
            <line x1="40" y1="60" x2="980" y2="60" stroke="#f0ebe0" stroke-dasharray="3 3"/>
            <line x1="40" y1="100" x2="980" y2="100" stroke="#f0ebe0" stroke-dasharray="3 3"/>
            <line x1="40" y1="140" x2="980" y2="140" stroke="#f0ebe0"/>

            <!-- Y Axis labels left -->
            <text x="25" y="24" fill="#a49f93" font-size="10" text-anchor="end">30</text>
            <text x="25" y="64" fill="#a49f93" font-size="10" text-anchor="end">20</text>
            <text x="25" y="104" fill="#a49f93" font-size="10" text-anchor="end">10</text>
            <text x="25" y="142" fill="#a49f93" font-size="10" text-anchor="end">0</text>

            <!-- Y Axis labels right (Percentage) -->
            <text x="990" y="24" fill="#c0362c" font-size="10">15%</text>
            <text x="990" y="64" fill="#c0362c" font-size="10">10%</text>
            <text x="990" y="104" fill="#c0362c" font-size="10">5%</text>
            <text x="990" y="142" fill="#c0362c" font-size="10">0%</text>

            <!-- 14 Date Columns (Assets Reviewed Bars) -->
            <!-- 10 Oct -->
            <rect x="70" y="80" width="22" height="60" rx="3" fill="#ebdcb9" opacity="0.8"/>
            <text x="81" y="155" fill="#8c887d" font-size="9.5" text-anchor="middle">10 Oct</text>

            <!-- 11 Oct -->
            <rect x="135" y="75" width="22" height="65" rx="3" fill="#ebdcb9" opacity="0.8"/>
            <text x="146" y="155" fill="#8c887d" font-size="9.5" text-anchor="middle">11 Oct</text>

            <!-- 12 Oct -->
            <rect x="200" y="70" width="22" height="70" rx="3" fill="#ebdcb9" opacity="0.8"/>
            <text x="211" y="155" fill="#8c887d" font-size="9.5" text-anchor="middle">12 Oct</text>

            <!-- 13 Oct -->
            <rect x="265" y="75" width="22" height="65" rx="3" fill="#ebdcb9" opacity="0.8"/>
            <text x="276" y="155" fill="#8c887d" font-size="9.5" text-anchor="middle">13 Oct</text>

            <!-- 14 Oct -->
            <rect x="330" y="85" width="22" height="55" rx="3" fill="#ebdcb9" opacity="0.8"/>
            <text x="341" y="155" fill="#8c887d" font-size="9.5" text-anchor="middle">14 Oct</text>

            <!-- 15 Oct -->
            <rect x="395" y="65" width="22" height="75" rx="3" fill="#ebdcb9" opacity="0.8"/>
            <text x="406" y="155" fill="#8c887d" font-size="9.5" text-anchor="middle">15 Oct</text>

            <!-- 16 Oct (Peak) -->
            <rect x="460" y="45" width="22" height="95" rx="3" fill="#ebdcb9" opacity="0.9"/>
            <text x="471" y="155" fill="#8c887d" font-size="9.5" text-anchor="middle">16 Oct</text>

            <!-- 17 Oct -->
            <rect x="525" y="80" width="22" height="60" rx="3" fill="#ebdcb9" opacity="0.8"/>
            <text x="536" y="155" fill="#8c887d" font-size="9.5" text-anchor="middle">17 Oct</text>

            <!-- 18 Oct -->
            <rect x="590" y="75" width="22" height="65" rx="3" fill="#ebdcb9" opacity="0.8"/>
            <text x="601" y="155" fill="#8c887d" font-size="9.5" text-anchor="middle">18 Oct</text>

            <!-- 19 Oct -->
            <rect x="655" y="85" width="22" height="55" rx="3" fill="#ebdcb9" opacity="0.8"/>
            <text x="666" y="155" fill="#8c887d" font-size="9.5" text-anchor="middle">19 Oct</text>

            <!-- 20 Oct -->
            <rect x="720" y="80" width="22" height="60" rx="3" fill="#ebdcb9" opacity="0.8"/>
            <text x="731" y="155" fill="#8c887d" font-size="9.5" text-anchor="middle">20 Oct</text>

            <!-- 21 Oct -->
            <rect x="785" y="75" width="22" height="65" rx="3" fill="#ebdcb9" opacity="0.8"/>
            <text x="796" y="155" fill="#8c887d" font-size="9.5" text-anchor="middle">21 Oct</text>

            <!-- 22 Oct -->
            <rect x="850" y="70" width="22" height="70" rx="3" fill="#ebdcb9" opacity="0.8"/>
            <text x="861" y="155" fill="#8c887d" font-size="9.5" text-anchor="middle">22 Oct</text>

            <!-- 23 Oct -->
            <rect x="915" y="75" width="22" height="65" rx="3" fill="#ebdcb9" opacity="0.9"/>
            <text x="926" y="155" fill="#8c887d" font-size="9.5" text-anchor="middle">24 Oct</text>

            <!-- Overlaid Bezier Curve (Violation Rate Dropping) -->
            <path d="M 81 128 Q 200 135 341 130 T 601 125 T 666 98 T 731 98 T 796 122 T 861 128 T 926 130" fill="none" stroke="#c0362c" stroke-width="2.5" stroke-linecap="round"/>
            
            <!-- Key point dots on the red curve -->
            <circle cx="81" cy="128" r="4" fill="#c0362c" stroke="#ffffff" stroke-width="2"/>
            <circle cx="211" cy="132" r="4" fill="#c0362c" stroke="#ffffff" stroke-width="2"/>
            <circle cx="341" cy="130" r="4" fill="#c0362c" stroke="#ffffff" stroke-width="2"/>
            <circle cx="471" cy="132" r="4" fill="#c0362c" stroke="#ffffff" stroke-width="2"/>
            <circle cx="601" cy="125" r="4" fill="#c0362c" stroke="#ffffff" stroke-width="2"/>
            <circle cx="666" cy="98" r="5" fill="#c0362c" stroke="#ffffff" stroke-width="2"/>
            <circle cx="731" cy="98" r="5" fill="#c0362c" stroke="#ffffff" stroke-width="2"/>
            <circle cx="796" cy="122" r="4" fill="#c0362c" stroke="#ffffff" stroke-width="2"/>
            <circle cx="861" cy="128" r="4" fill="#c0362c" stroke="#ffffff" stroke-width="2"/>
            <circle cx="926" cy="130" r="4" fill="#c0362c" stroke="#ffffff" stroke-width="2"/>
          </svg>
        </div>
      </div>
    </div>

    <!-- ==================== SUB-VIEWS (INTEGRATED FULL SUITE) ==================== -->
    
    <!-- SUB-VIEW: CONTENT REVIEW (3-TIER REMEDIATION) -->
    <div class="content-body tab-page" id="view-review">
      <div class="welcome-row">
        <div>
          <h1 class="headline-serif">Content Review & Remediation</h1>
          <p class="headline-sub">AI-driven clause-by-clause audit with 3-tier voice-adaptive remediation.</p>
        </div>
        <button class="btn-luxury-dark" onclick="runTextAudit()">⚡ Audit Active Draft</button>
      </div>

      <div style="display:grid; grid-template-columns:1fr 1fr; gap:24px; margin-bottom:24px;">
        <div class="luxury-card">
          <h3 class="card-headline" style="margin-bottom:12px;">Draft Marketing Content</h3>
          <textarea id="draftTextarea" style="width:100%; height:260px; padding:16px; border:1px solid var(--card-border); border-radius:var(--radius-sm); font-size:14px; line-height:1.6; outline:none; resize:none;">Our revolutionary new serum cures adult acne permanently and eliminates blemishes overnight! Clinically proven to transform damaged skin with 100% guaranteed results. Buy now before stock runs out, you don't want to be left with terrible skin!</textarea>
          <div style="display:flex; justify-content:space-between; align-items:center; margin-top:14px;">
            <span style="font-size:12px; color:var(--ink-subtle);">Word count: 39 | Language: English</span>
            <button class="btn-luxury-dark" onclick="runTextAudit()">Scan for Violations</button>
          </div>
        </div>

        <div class="luxury-card">
          <h3 class="card-headline" style="margin-bottom:12px;">Detected Regulatory Findings</h3>
          <div id="findingsListView" style="display:flex; flex-direction:column; gap:12px; max-height:280px; overflow-y:auto;">
            <!-- Dynamically populated findings -->
          </div>
        </div>
      </div>

      <!-- 3-TIER REMEDIATION SECTION -->
      <div class="luxury-card">
        <h3 class="card-headline" style="margin-bottom:6px;">✨ Context-Preserving Smart Remediation (Multi-Tier)</h3>
        <p class="card-caption" style="margin-bottom:18px;">Select a tailored rewrite option that preserves brand voice while eliminating legal liability.</p>
        
        <div id="remediationCardTiers" style="display:flex; flex-direction:column; gap:14px;">
          <!-- Populated dynamically with Tier 1, 2, 3 -->
        </div>
      </div>
    </div>

    <!-- SUB-VIEW: CREATIVE AUDIT (MULTIMODAL VISION) -->
    <div class="content-body tab-page" id="view-creative">
      <div class="welcome-row">
        <div>
          <h1 class="headline-serif">Multimodal Creative Vision</h1>
          <p class="headline-sub">Computer vision audit of image assets for logo safety, brand palette, and WCAG contrast.</p>
        </div>
        <div style="display:flex; gap:10px;">
          <button class="dropdown-trigger" onclick="loadSampleCreative('skincare')">Sample Skincare Banner</button>
          <button class="dropdown-trigger" onclick="loadSampleCreative('fintech')">Sample Fintech Creative</button>
        </div>
      </div>

      <div style="display:grid; grid-template-columns:1.2fr 0.8fr; gap:24px;">
        <div class="luxury-card" style="align-items:center; justify-content:center; background:#f4f0e6;">
          <canvas id="creativeCanvas" width="580" height="380" style="max-width:100%; border-radius:10px; box-shadow:var(--shadow-card);"></canvas>
        </div>

        <div class="luxury-card">
          <h3 class="card-headline" style="margin-bottom:14px;">Diagnostic Visual Scorecard</h3>
          <div id="visionReportBox" style="display:flex; flex-direction:column; gap:14px;">
            <!-- Vision findings -->
          </div>
        </div>
      </div>
    </div>

    <!-- SUB-VIEW: LIVE INTERCEPTOR (SHOWSTOPPER) -->
    <div class="content-body tab-page" id="view-interceptor">
      <div class="welcome-row">
        <div>
          <h1 class="headline-serif">Live Interceptor Lab</h1>
          <p class="headline-sub">Real-time browser extension simulator intercepting rogue drafts inside social composers.</p>
        </div>
      </div>

      <div style="max-width:680px; margin:0 auto;" class="luxury-card">
        <div style="display:flex; align-items:center; gap:12px; margin-bottom:16px;">
          <div style="width:42px; height:42px; border-radius:50%; background:#17181f; color:#fff; display:grid; place-items:center; font-weight:700;">NS</div>
          <div>
            <strong style="font-size:14px;">Northstar Skincare Official</strong>
            <div style="font-size:12px; color:var(--ink-subtle);">@NorthstarSkin &bull; Brand Marketing</div>
          </div>
        </div>

        <div style="position:relative;">
          <textarea id="liveTweetBox" style="width:100%; height:130px; border:1px solid var(--card-border); border-radius:var(--radius-sm); padding:16px; font-size:15px; line-height:1.5; outline:none; resize:none;" oninput="onLiveTweetInput()">Our new serum cures acne permanently overnight with guaranteed 100% results! Buy now before your skin gets worse!</textarea>
          
          <div id="floatingShield" style="position:absolute; right:14px; bottom:14px; background:#121316; color:#fff; padding:6px 14px; border-radius:20px; font-size:12px; font-weight:700; display:flex; align-items:center; gap:8px; cursor:pointer; box-shadow:0 4px 14px rgba(0,0,0,0.3); border:1px solid #c0362c;" onclick="autoFixLiveTweet()">
            <span>🛡️</span>
            <span id="shieldMsg">2 Risks Intercepted</span>
            <span style="background:var(--status-red); color:#fff; padding:2px 7px; border-radius:10px; font-size:10px;">AUTO-FIX</span>
          </div>
        </div>

        <div style="display:flex; justify-content:space-between; align-items:center; margin-top:18px; border-top:1px solid #f0ebe0; padding-top:14px;">
          <span style="font-size:13px; color:var(--ink-subtle);">Pre-Publication Shield Active</span>
          <button class="btn-luxury-dark" id="btnPublishTweet" disabled style="opacity:0.5;">Publish Post</button>
        </div>
      </div>
    </div>

    <!-- SUB-VIEW: ADVERSARIAL RED-TEAM TEST -->
    <div class="content-body tab-page" id="view-adversarial">
      <div class="welcome-row">
        <div>
          <h1 class="headline-serif">Adversarial PR Red-Teaming</h1>
          <p class="headline-sub">Autonomous multi-agent attack simulating Lanham Act lawsuits, viral consumer outrage, and FTC fines.</p>
        </div>
        <button class="btn-luxury-dark" onclick="alert('Red-team simulation executed. Vulnerability matrix refreshed.')">🔥 Re-run Stress Test</button>
      </div>

      <div class="luxury-card" style="background:#171822; color:#fff; border:1px solid #282a38; margin-bottom:24px;">
        <div style="color:#ff6b6b; font-size:11px; font-weight:800; text-transform:uppercase; letter-spacing:1px; margin-bottom:6px;">Simulated Crisis Breaking News Banner</div>
        <h2 style="font-family:'Fraunces', serif; font-size:24px; color:#ffffff; line-height:1.2; margin-bottom:8px;">"SKINCARE BRAND FACES RECORD FTC INVESTIGATION OVER UNPROVEN MEDICAL CLAIMS"</h2>
        <p style="color:#a8abb8; font-size:13px;">Regulatory watchdog demands immediate corrective advertising campaign following deceptive pre-market assertion.</p>
      </div>

      <div style="display:grid; grid-template-columns:repeat(3, 1fr); gap:18px;">
        <div class="luxury-card" style="border-top:3px solid var(--status-red);">
          <strong style="color:var(--status-red); font-size:14px;">1. Competitor Legal Counsel</strong>
          <p style="font-size:12px; color:var(--ink-secondary); margin:8px 0;">Drafts cease-and-desist under Lanham Act §43(a) citing deceptive efficacy assertions.</p>
          <div style="background:#f9f6ef; padding:10px; border-radius:6px; font-size:11.5px; font-family:'JetBrains Mono';">"Your assertion of 'eradicating acne permanently' lacks double-blind vehicle control. Demand immediate recall."</div>
        </div>

        <div class="luxury-card" style="border-top:3px solid var(--status-amber);">
          <strong style="color:var(--status-amber); font-size:14px;">2. Viral Consumer Outrage</strong>
          <p style="font-size:12px; color:var(--ink-secondary); margin:8px 0;">Simulates Twitter quote-tweets and boycott virality risk.</p>
          <div style="background:#f9f6ef; padding:10px; border-radius:6px; font-size:11.5px; font-family:'JetBrains Mono';">"Imagine paying $40 for a serum that claims to cure acne in 24 hours 🤡 #BoycottNorthstar #SkinScam"</div>
        </div>

        <div class="luxury-card" style="border-top:3px solid #2563eb;">
          <strong style="color:#2563eb; font-size:14px;">3. Regulatory Enforcement</strong>
          <p style="font-size:12px; color:var(--ink-secondary); margin:8px 0;">Calculates statutory civil monetary penalties.</p>
          <div style="background:#f9f6ef; padding:10px; border-radius:6px; font-size:11.5px; font-family:'JetBrains Mono';">"Projected Civil Penalty: $51,744 per violation under 15 U.S.C. § 45(m)(1)(A)."</div>
        </div>
      </div>
    </div>

  </main>
</div>

<!-- ==================== SLIDING INSPECTION DRAWER ==================== -->
<div class="drawer-backdrop" id="inspectionDrawer" onclick="closeDrawer(event)">
  <div class="drawer-panel" onclick="event.stopPropagation()">
    <div class="drawer-header">
      <div>
        <h3 class="card-headline" id="drawerTitle">Asset Review Details</h3>
        <p class="card-caption" id="drawerMeta">Detailed compliance report & citations</p>
      </div>
      <button onclick="closeDrawerDirect()" style="font-size:20px; color:#888;">✕</button>
    </div>
    <div class="drawer-body" id="drawerContent">
      <!-- Populated dynamically -->
    </div>
  </div>
</div>

<script>
// NAVIGATION CONTROLLER
function switchNav(viewId, element) {
  document.querySelectorAll('.tab-page').forEach(p => p.classList.remove('active'));
  document.querySelectorAll('.nav-link').forEach(l => l.classList.remove('active'));

  const target = document.getElementById('view-' + viewId);
  if (target) {
    target.classList.add('active');
  } else {
    // Fallback to dashboard if view doesn't exist
    document.getElementById('view-dashboard').classList.add('active');
  }

  if (element) {
    element.classList.add('active');
  } else {
    // Find matching button
    document.querySelectorAll('.nav-link').forEach(btn => {
      if (btn.getAttribute('onclick') && btn.getAttribute('onclick').includes(viewId)) {
        btn.classList.add('active');
      }
    });
  }

  if (viewId === 'creative') {
    setTimeout(drawSampleSkincare, 50);
  } else if (viewId === 'review') {
    runTextAudit();
  }
}

// NUMBER COUNTER ANIMATION
window.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('.counter').forEach(el => {
    const target = +el.getAttribute('data-target');
    let count = 0;
    const speed = 25;
    const inc = target / speed;
    const update = () => {
      count += inc;
      if (count < target) {
        el.innerText = Math.ceil(count);
        setTimeout(update, 20);
      } else {
        el.innerText = target;
      }
    };
    update();
  });

  drawSampleSkincare();
  runTextAudit();
});

// DRAWER INSPECTOR
function inspectRow(title, status, violations, meta) {
  document.getElementById('drawerTitle').innerText = title;
  document.getElementById('drawerMeta').innerText = meta;
  
  const content = document.getElementById('drawerContent');
  content.innerHTML = `
    <div style="display:flex; justify-content:space-between; align-items:center; padding:14px; background:#faf7f0; border-radius:8px; border:1px solid #eee8dc;">
      <div>
        <span style="font-size:12px; color:#888;">Compliance Status</span>
        <div style="font-weight:700; font-size:15px; margin-top:2px;">${status}</div>
      </div>
      <span class="status-pill ${status === 'Needs Review' ? 'pill-needs-review' : status === 'High Risk' ? 'pill-high-risk' : 'pill-compliant'}">${status}</span>
    </div>

    <div>
      <strong style="font-size:13px; text-transform:uppercase; letter-spacing:0.5px; color:#888;">Flagged Violations (${violations})</strong>
      <div style="margin-top:10px; display:flex; flex-direction:column; gap:10px;">
        ${violations > 0 ? `
          <div style="background:#fff; border:1px solid #f0e6dc; border-left:3px solid #c0362c; padding:12px; border-radius:6px; font-size:13px;">
            <div style="font-weight:700; color:#c0362c;">21 CFR § 701.3 Medical Drug Claim</div>
            <div style="color:#666; font-size:12px; margin-top:4px;">Draft claims product 'cures acne permanently', converting cosmetic into unapproved new drug.</div>
          </div>
        ` : `
          <div style="color:#227a51; font-weight:600; font-size:13px;">Zero violations detected. Asset is publish-ready!</div>
        `}
      </div>
    </div>

    <div style="margin-top:auto; padding-top:20px; border-top:1px solid #eee; display:flex; gap:12px;">
      <button class="btn-luxury-dark" style="flex:1;" onclick="switchNav('review', null); closeDrawerDirect();">Open in Content Reviewer →</button>
    </div>
  `;

  document.getElementById('inspectionDrawer').classList.add('open');
}

function closeDrawer(e) {
  if (e.target.id === 'inspectionDrawer') {
    closeDrawerDirect();
  }
}
function closeDrawerDirect() {
  document.getElementById('inspectionDrawer').classList.remove('open');
}

function openReviewModal() {
  switchNav('review', null);
}

function openBrandModal() {
  alert('Active Brand: Northstar Skincare (Enterprise License). To switch to PulsePay or Aster & Oak, select from settings.');
}

// MULTIMODAL CANVAS DRAWING
function drawSampleSkincare() {
  const canvas = document.getElementById('creativeCanvas');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');

  // Background
  ctx.fillStyle = '#28704E';
  ctx.fillRect(0, 0, canvas.width, canvas.height);

  // Gradient Overlay
  const grad = ctx.createLinearGradient(0, 0, canvas.width, canvas.height);
  grad.addColorStop(0, 'rgba(255,255,255,0.08)');
  grad.addColorStop(1, 'rgba(0,0,0,0.3)');
  ctx.fillStyle = grad;
  ctx.fillRect(0, 0, canvas.width, canvas.height);

  // Logo
  ctx.fillStyle = '#ffffff';
  ctx.font = 'bold 22px Fraunces, serif';
  ctx.fillText('Northstar Skincare ✦', 40, 55);

  // Headline
  ctx.font = 'bold 26px Plus Jakarta Sans, sans-serif';
  ctx.fillText('Pure 2% Niacinamide Serum', 40, 140);

  // Banned Red Accent (Violation Box)
  ctx.fillStyle = '#FF1744';
  ctx.fillRect(40, 168, 250, 40);
  ctx.fillStyle = '#ffffff';
  ctx.font = 'bold 15px Plus Jakarta Sans, sans-serif';
  ctx.fillText('⚡ 100% CURES ACNE NOW', 52, 193);

  // Safe Margin Border (Yellow dotted)
  ctx.strokeStyle = '#dfb76c';
  ctx.lineWidth = 1.5;
  ctx.setLineDash([5, 5]);
  ctx.strokeRect(30, 25, canvas.width - 60, canvas.height - 50);
  ctx.setLineDash([]);

  // Disclaimer Fine Print (Low contrast)
  ctx.fillStyle = '#39634f';
  ctx.font = '10px Plus Jakarta Sans, sans-serif';
  ctx.fillText('*Results not evaluated by FDA. Individual results vary. Verified trial NCT0482910.', 40, 345);

  // Render report
  document.getElementById('visionReportBox').innerHTML = `
    <div style="background:#faf7f0; padding:12px; border-radius:8px; border:1px solid #eee8dc;">
      <div style="display:flex; justify-content:space-between; align-items:center;">
        <strong style="font-size:13px;">Brand Color Palette Compliance</strong>
        <span class="status-pill pill-needs-review">Off-Brand Color</span>
      </div>
      <p style="font-size:12px; color:#666; margin-top:4px;">Detected unauthorized neon red accent <code>#FF1744</code>. Northstar palette strictly prohibits high-saturation red badges.</p>
    </div>

    <div style="background:#faf7f0; padding:12px; border-radius:8px; border:1px solid #eee8dc;">
      <div style="display:flex; justify-content:space-between; align-items:center;">
        <strong style="font-size:13px;">OCR Disclaimer Contrast (WCAG 2.1)</strong>
        <span class="status-pill pill-in-review">1.9 : 1 (Fail)</span>
      </div>
      <p style="font-size:12px; color:#666; margin-top:4px;">Mandatory disclaimer font at bottom fails minimum contrast threshold of 4.5:1.</p>
    </div>
  `;
}

function loadSampleCreative(type) {
  drawSampleSkincare();
}

// 3-TIER REMEDIATION AUDIT
function runTextAudit() {
  const findingsBox = document.getElementById('findingsListView');
  const tiersBox = document.getElementById('remediationCardTiers');
  if (!findingsBox || !tiersBox) return;

  findingsBox.innerHTML = `
    <div style="border:1px solid #fad5d3; background:#fdf0ef; padding:12px; border-radius:8px;">
      <div style="display:flex; justify-content:space-between;">
        <strong style="color:#c0362c; font-size:13px;">FDA Medical Drug Boundary (21 CFR § 701.3)</strong>
        <span class="status-pill pill-high-risk">Critical</span>
      </div>
      <p style="font-size:12px; color:#555; margin-top:4px;">Word "cures adult acne permanently" converts cosmetic into an unapproved new drug.</p>
    </div>

    <div style="border:1px solid #fbe5c5; background:#fef5e7; padding:12px; border-radius:8px;">
      <div style="display:flex; justify-content:space-between;">
        <strong style="color:#b86e00; font-size:13px;">FTC Unsubstantiated Guarantee (16 CFR Part 255)</strong>
        <span class="status-pill pill-in-review">High</span>
      </div>
      <p style="font-size:12px; color:#555; margin-top:4px;">"100% guaranteed results" requires certified randomized double-blind clinical trial.</p>
    </div>
  `;

  tiersBox.innerHTML = `
    <!-- Tier 1 -->
    <div style="border:1px solid #c9ecda; background:#f4fbf7; padding:16px; border-radius:10px;">
      <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
        <span style="font-weight:700; font-size:13px; color:#227a51;">🛡️ Tier 1: Conservative Safe-Harbor (Zero-Risk Compliance)</span>
        <button class="btn-luxury-dark" style="font-size:11px; padding:4px 10px;" onclick="applyTier(1)">Apply Rewrite</button>
      </div>
      <p style="font-size:13px; line-height:1.6; color:#2b2c34;">
        Our new serum <span style="background:#d1fae5; color:#065f46; font-weight:700; padding:2px 4px; border-radius:3px;">helps visibly improve the appearance of acne-prone skin</span> and soothes blemishes overnight. Designed to support a clearer complexion. Discover a gentle addition to your daily skincare routine.
      </p>
    </div>

    <!-- Tier 2 -->
    <div style="border:1px solid #e2dbce; background:#ffffff; padding:16px; border-radius:10px;">
      <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
        <span style="font-weight:700; font-size:13px; color:#b68735;">⚡ Tier 2: Balanced High-Converting (Brand Voice Optimized)</span>
        <button class="btn-luxury-dark" style="font-size:11px; padding:4px 10px;" onclick="applyTier(2)">Apply Rewrite</button>
      </div>
      <p style="font-size:13px; line-height:1.6; color:#2b2c34;">
        Our revolutionary serum <span style="background:#fef3c7; color:#92400e; font-weight:700; padding:2px 4px; border-radius:3px;">visibly targets stubborn blemishes</span> with notice-worthy results. Clinically tested 2% Niacinamide formula backed by user satisfaction testing. Elevate your barrier health today!
      </p>
    </div>
  `;
}

function applyTier(num) {
  const ta = document.getElementById('draftTextarea');
  if (num === 1) {
    ta.value = "Our new serum helps visibly improve the appearance of acne-prone skin and soothes blemishes overnight. Designed to support a clearer complexion. Discover a gentle addition to your daily skincare routine.";
  } else {
    ta.value = "Our revolutionary serum visibly targets stubborn blemishes with notice-worthy results. Clinically tested 2% Niacinamide formula backed by user satisfaction testing. Elevate your barrier health today!";
  }
  alert(`Tier ${num} successfully applied! Draft updated with 0 regulatory violations.`);
}

// LIVE INTERCEPTOR TYPING
function onLiveTweetInput() {
  const text = document.getElementById('liveTweetBox').value;
  const shield = document.getElementById('floatingShield');
  const shieldMsg = document.getElementById('shieldMsg');
  const pubBtn = document.getElementById('btnPublishTweet');

  const hasCure = /cures?|eliminates?|guaranteed/i.test(text);
  if (hasCure) {
    shield.style.borderColor = '#c0362c';
    shieldMsg.innerText = '2 Risks Intercepted';
    pubBtn.disabled = true;
    pubBtn.style.opacity = '0.5';
  } else {
    shield.style.borderColor = '#227a51';
    shieldMsg.innerText = '100% Compliant';
    pubBtn.disabled = false;
    pubBtn.style.opacity = '1';
  }
}

function autoFixLiveTweet() {
  document.getElementById('liveTweetBox').value = "Discover our dermatologically formulated 2% Niacinamide Serum, designed to support a calm and healthy-looking skin barrier. Backed by verified clinical study NCT0482910. #NorthstarSkin";
  onLiveTweetInput();
  alert('⚡ Clauze Interceptor surgically auto-fixed the tweet in place! Post is now 100% compliant and ready to publish.');
}
</script>
</body>
</html>
'''

# Write to both index.html and dist/index.html so live tunnel updates immediately!
targets = [
    r'C:\Users\sahil\.gemini\antigravity\scratch\Clauze_AI_Enterprise\index.html',
    r'C:\Users\sahil\.gemini\antigravity\scratch\Clauze_AI_Enterprise\dist\index.html'
]

for t in targets:
    with open(t, 'w', encoding='utf-8') as f:
        f.write(html_code)
    print(f"Updated {t} ({len(html_code)} bytes)")

