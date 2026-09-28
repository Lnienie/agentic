custom_css = """
    /* ============================================
       MAIN CONTAINER
       ============================================ */
    .progress-text { 
        display: none !important;
    }
    
    .gradio-container { 
        max-width: 1000px !important;
        width: 100% !important;
        margin: 0 auto !important;
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', sans-serif;
        background: #eef4fb !important;
        color: #1f2937 !important;
    }
    
    /* ============================================
       TABS
       ============================================ */
    button[role="tab"] {
        color: #64748b !important;
        border-bottom: 2px solid transparent !important;
        border-radius: 0 !important;
        transition: all 0.2s ease !important;
        background: transparent !important;
    }
    
    button[role="tab"]:hover {
        color: #1d4ed8 !important;
    }
    
    button[role="tab"][aria-selected="true"] {
        color: #1d4ed8 !important;
        border-bottom: 2px solid #2563eb !important;
        border-radius: 0 !important;
        background: transparent !important;
    }
    
    .tabs {
        border-bottom: none !important;
        border-radius: 0 !important;
    }
    
    .tab-nav {
        border-bottom: 1px solid #dbe3ee !important;
        border-radius: 0 !important;
    }
    
    button[role="tab"]::before,
    button[role="tab"]::after,
    .tabs::before,
    .tabs::after,
    .tab-nav::before,
    .tab-nav::after {
        display: none !important;
        content: none !important;
        border-radius: 0 !important;
    }
    
    #doc-management-tab {
        max-width: 500px !important;
        margin: 0 auto !important;
    }
    
    /* ============================================
       BUTTONS
       ============================================ */
    button {
        border-radius: 8px !important;
        border: none !important;
        font-weight: 500 !important;
        transition: all 0.2s ease !important;
        box-shadow: none !important;
    }
    
    .primary {
        background: #3b82f6 !important;
        color: white !important;
    }
    
    .primary:hover {
        background: #2563eb !important;
        transform: translateY(-1px) !important;
    }
    
    .stop {
        background: #ef4444 !important;
        color: white !important;
    }
    
    .stop:hover {
        background: #dc2626 !important;
        transform: translateY(-1px) !important;
    }
    
    /* ============================================
       CHAT INPUT BOX
       ============================================ */
    textarea[placeholder="Type a message..."],
    textarea[data-testid*="textbox"]:not(#file-list-box textarea) {
        background: transparent !important;
        border: none !important;
        box-shadow: none !important;
    }
    
    textarea[placeholder="Type a message..."]:focus {
        background: transparent !important;
        border: none !important;
        box-shadow: none !important;
    }
    
    .gr-text-input:has(textarea[placeholder="Type a message..."]),
    [class*="chatbot"] + * [data-testid="textbox"],
    form:has(textarea[placeholder="Type a message..."]) > div {
        background: transparent !important;
        border: none !important;
        gap: 12px !important;
    }
    
    form:has(textarea[placeholder="Type a message..."]) button,
    [class*="chatbot"] ~ * button[type="submit"] {
        background: transparent !important;
        border: none !important;
        padding: 8px !important;
    }
    
    form:has(textarea[placeholder="Type a message..."]) button:hover {
        background: rgba(59, 130, 246, 0.1) !important;
    }
    
    form:has(textarea[placeholder="Type a message..."]) {
        gap: 12px !important;
        display: flex !important;
    }
    
    /* ============================================
       FILE UPLOAD
       ============================================ */
    .file-preview, 
    [data-testid="file-upload"] {
        background: #ffffff !important;
        border: 1px solid #cbd5e1 !important;
        border-radius: 5px !important;
        color: #ffffff !important;
        min-height: 200px !important;
    }
    
    .file-preview:hover, 
    [data-testid="file-upload"]:hover {
        border-color: #3b82f6 !important;
        background: #f8fbff !important;
    }
    
    .file-preview *,
    [data-testid="file-upload"] * {
        color: #334155 !important;
    }
    
    .file-preview .label,
    [data-testid="file-upload"] .label {
        display: none !important;
    }
    
    /* ============================================
       INPUTS & TEXTAREAS
       ============================================ */
    input, 
    textarea {
        background: #ffffff !important;
        border: 1px solid #cbd5e1 !important;
        border-radius: 10px !important;
        color: #1f2937 !important;
        transition: border-color 0.2s ease !important;
    }
    
    input:focus, 
    textarea:focus {
        border-color: #3b82f6 !important;
        outline: none !important;
        box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.1) !important;
    }
    
    textarea[readonly] {
        background: #f8fafc !important;
        color: #64748b !important;
    }
    
    /* ============================================
       FILE LIST BOX
       ============================================ */
    #file-list-box {
        background: #ffffff !important;
        border: 1px solid #cbd5e1 !important;
        border-radius: 5px !important;
        padding: 10px !important;
    }
    
    #file-list-box textarea {
        background: transparent !important;
        border: none !important;
        color: #334155 !important;
        padding: 0 !important;
    }
    
    /* ============================================
       CHATBOT CONTAINER
       ============================================ */
    .chatbot {
        border-radius: 12px !important;
        background: #ffffff !important;
        border: 1px solid #dbe3ee !important;
        box-shadow: 0 8px 24px rgba(30, 64, 175, 0.08) !important;
    }

    .chatbot .message-wrap,
    .chatbot > div {
        gap: 8px !important;
        padding: 12px !important;
    }

    /* ============================================
       MESSAGE BUBBLES
       ============================================ */
    .message {
        border-radius: 10px !important;
    }

    .message.user {
        background: #dbeafe !important;
        color: #111827 !important;
        border: 1px solid #bfdbfe !important;
    }

    .message.user * {
        color: #111827 !important;
    }
    
    .message.bot {
        background: #f8fafc !important;
        color: #1f2937 !important;
        border: 1px solid #dbe3ee !important;
        width: fit-content !important;
        max-width: 90% !important;
    }
    
    .message-row img {
        margin: 0px !important;
    }

    .avatar-container img {
        padding: 0px !important;
    }

    /* ============================================
       PROGRESS BAR
       ============================================ */
    .progress-bar-wrap {
        border-radius: 10px !important;
        overflow: hidden !important;
        background: #e2e8f0 !important;
    }

    .progress-bar {
        border-radius: 10px !important;
        background: #3b82f6 !important;
    }
    
    /* ============================================
       TYPOGRAPHY
       ============================================ */
    h1, h2, h3, h4, h5, h6 {
        color: #172554 !important;
    }

    p, label, .prose {
        color: #475569 !important;
    }

    ::placeholder {
        color: #94a3b8 !important;
        opacity: 1 !important;
    }
    
    /* ============================================
       GLOBAL OVERRIDES
       ============================================ */
    body {
        background: #eef4fb !important;
    }

    footer {
        visibility: hidden;
    }
"""