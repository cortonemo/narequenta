/* Nárëquenta PC Sheet Styles v0.2 */

body {
    font-family: 'Georgia', serif;
    color: #333;
    background-color: #f8f8f8;
    padding: 20px;
    max-width: 800px;
    margin: 0 auto;
}

header h1 {
    color: #5d4037;
    border-bottom: 2px solid #5d4037;
    padding-bottom: 5px;
    text-align: center;
}

.essence-grid {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr 1fr 1fr 1fr 1fr;
    gap: 10px;
    margin-bottom: 20px;
    align-items: center;
    font-size: 14px;
}

.essence-grid-header {
    font-weight: bold;
    text-align: center;
    padding: 5px 0;
    border-bottom: 1px solid #ccc;
}

input[type="number"] {
    width: 90%;
    padding: 3px;
    text-align: center;
    border: 1px solid #ccc;
}

/* Section Headers (e.g., Essences, Promise) */
.section-header {
    background-color: #5d4037;
    color: white;
    padding: 5px;
    margin-top: 15px;
    font-weight: bold;
    text-align: center;
}

/* General info block (Name/HP) */
.info-block {
    padding: 10px;
    border: 1px solid #5d4037;
    margin-bottom: 10px;
}

/* Read-Only Fields */
.read-only {
    background-color: #eee;
    color: #555;
    cursor: default;
}

/* Abilities Table Styling */
.abilities-table {
    width: 100%; 
    border-collapse: collapse; 
    margin-bottom: 20px;
}

.abilities-table thead tr {
    background-color: #6d4c41; 
    color: white;
}

.abilities-table th, .abilities-table td {
    padding: 5px; 
    border: 1px solid #555; /* Use 555 for table lines */
    text-align: left;
}

.abilities-table tbody tr {
    background-color: white;
}

.abilities-table tbody tr:nth-child(even) {
    background-color: #f7f7f7; /* Alternating row color */
}

/* Special Rows (Cantrip/Spell Titles) */
.abilities-table tr.utility-row td {
    background-color: #f0f0f0;
    text-align: center;
    font-weight: bold;
}

.abilities-table tr.magic-row td {
    background-color: #6d4c41; 
    color: white;
    text-align: center;
    font-weight: bold;
}