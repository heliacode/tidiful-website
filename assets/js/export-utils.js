/**
 * Export Utilities for Tidiful Data Grid
 * Handles CSV, JSON, Excel, and HTML exports
 */

class ExportUtils {
    constructor() {
        this.timestamp = new Date().toISOString().split('T')[0];
    }

    /**
     * Export data in specified format
     * @param {Array} data - Array of invoice/expense objects
     * @param {string} format - Export format: 'csv', 'json', 'excel', 'html', 'docx', 'pdf', 'qif', 'iif', 'xml'
     * @param {Function} formatDate - Date formatting function
     */
    exportData(data, format, formatDate) {
        switch (format) {
            case 'csv':
                this.exportCSV(data);
                break;
            case 'json':
                this.exportJSON(data);
                break;
            case 'excel':
                this.exportExcel(data);
                break;
            case 'html':
                this.exportHTML(data, formatDate);
                break;
            case 'docx':
                this.exportDOCX(data, formatDate);
                break;
            case 'pdf':
                this.exportPDF(data, formatDate);
                break;
            case 'qif':
                this.exportQIF(data, formatDate);
                break;
            case 'iif':
                this.exportIIF(data, formatDate);
                break;
            case 'xml':
                this.exportXML(data, formatDate);
                break;
            default:
                console.error('Unknown export format:', format);
        }
    }

    /**
     * Export data as CSV
     * @param {Array} data - Array of invoice/expense objects
     */
    exportCSV(data) {
        const headers = ['Invoice #', 'Date', 'Vendor', 'Amount', 'Tax Amount', 'Total Amount', 'Category'];
        const csvContent = [
            headers.join(','),
            ...data.map(invoice => [
                invoice.invoiceNumber || 'N/A',
                invoice.date || 'N/A',
                '"' + (invoice.vendor || 'N/A') + '"',
                invoice.amount || 0,
                invoice.taxAmount || 0,
                (invoice.amount || 0) + (invoice.taxAmount || 0),
                '"' + (invoice.category || 'N/A') + '"'
            ].join(','))
        ].join('\n');

        this.downloadFile(csvContent, 'text/csv;charset=utf-8;', 'expenses_' + this.timestamp + '.csv');
    }

    /**
     * Export data as JSON
     * @param {Array} data - Array of invoice/expense objects
     */
    exportJSON(data) {
        const jsonContent = JSON.stringify(data, null, 2);
        this.downloadFile(jsonContent, 'application/json;charset=utf-8;', 'expenses_' + this.timestamp + '.json');
    }

    /**
     * Export data as Excel
     * @param {Array} data - Array of invoice/expense objects
     */
    exportExcel(data) {
        if (typeof XLSX === 'undefined') {
            alert('Excel export not available. Please refresh the page and try again.');
            return;
        }

        const headers = ['Invoice #', 'Date', 'Vendor', 'Amount', 'Tax Amount', 'Total Amount', 'Category'];
        const excelData = [
            headers,
            ...data.map(invoice => [
                invoice.invoiceNumber || 'N/A',
                invoice.date || 'N/A',
                invoice.vendor || 'N/A',
                invoice.amount || 0,
                invoice.taxAmount || 0,
                (invoice.amount || 0) + (invoice.taxAmount || 0),
                invoice.category || 'N/A'
            ])
        ];

        const wb = XLSX.utils.book_new();
        const ws = XLSX.utils.aoa_to_sheet(excelData);
        
        // Set column widths
        ws['!cols'] = [
            { wch: 12 }, // Invoice #
            { wch: 12 }, // Date
            { wch: 20 }, // Vendor
            { wch: 12 }, // Amount
            { wch: 12 }, // Tax Amount
            { wch: 12 }, // Total Amount
            { wch: 15 }  // Category
        ];

        XLSX.utils.book_append_sheet(wb, ws, 'Expenses');
        XLSX.writeFile(wb, 'expenses_' + this.timestamp + '.xlsx');
    }

    /**
     * Export data as HTML report
     * @param {Array} data - Array of invoice/expense objects
     * @param {Function} formatDate - Date formatting function
     */
    exportHTML(data, formatDate) {
        const totals = this.calculateTotals(data);
        const today = new Date().toLocaleDateString('en-US', { 
            year: 'numeric', 
            month: 'long', 
            day: 'numeric' 
        });
        
        let html = '<!DOCTYPE html>' +
            '<html>' +
            '<head>' +
            '<title>Expense Report - ' + today + '</title>' +
            '<style>' +
            'body { font-family: Arial, sans-serif; margin: 20px; }' +
            'h1 { color: #2E7D32; text-align: center; }' +
            'table { border-collapse: collapse; width: 100%; margin: 20px 0; }' +
            'th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }' +
            'th { background-color: #f2f2f2; font-weight: bold; }' +
            '.footer { text-align: center; color: #666; font-style: italic; margin-top: 30px; }' +
            '.summary { background-color: #f9f9f9; padding: 15px; margin: 20px 0; border-radius: 5px; }' +
            '</style>' +
            '</head>' +
            '<body>' +
            '<h1>Expense Report</h1>' +
            '<p style="text-align: center; color: #666;">Generated on ' + today + '</p>' +
            '<div class="summary">' +
            '<h3>Summary</h3>' +
            '<p><strong>Total Expenses:</strong> $' + totals.grandTotal.toFixed(2) + '</p>' +
            '<p><strong>Number of Records:</strong> ' + totals.totalInvoices + '</p>' +
            '</div>' +
            '<table>' +
            '<thead>' +
            '<tr>' +
            '<th>Invoice #</th>' +
            '<th>Date</th>' +
            '<th>Vendor</th>' +
            '<th>Amount</th>' +
            '<th>Tax</th>' +
            '<th>Total</th>' +
            '<th>Category</th>' +
            '</tr>' +
            '</thead>' +
            '<tbody>';
        
        data.forEach(invoice => {
            const totalAmount = (invoice.amount || 0) + (invoice.taxAmount || 0);
            html += '<tr>' +
                '<td>' + (invoice.invoiceNumber || 'N/A') + '</td>' +
                '<td>' + formatDate(invoice.date) + '</td>' +
                '<td>' + (invoice.vendor || 'N/A') + '</td>' +
                '<td>$' + (invoice.amount || 0).toFixed(2) + '</td>' +
                '<td>$' + (invoice.taxAmount || 0).toFixed(2) + '</td>' +
                '<td>$' + totalAmount.toFixed(2) + '</td>' +
                '<td>' + (invoice.category || 'N/A') + '</td>' +
                '</tr>';
        });
        
        html += '</tbody>' +
            '</table>' +
            '<div class="footer">Created with tidiful.com</div>' +
            '</body>' +
            '</html>';
        
        this.downloadFile(html, 'text/html;charset=utf-8', 'expense_report_' + new Date().toISOString().slice(0, 19).replace(/:/g, '-') + '.html');
    }

    /**
     * Export data as DOCX-compatible HTML (can be opened in Word)
     * @param {Array} data - Array of invoice/expense objects
     * @param {Function} formatDate - Date formatting function
     */
    exportDOCX(data, formatDate) {
        try {
            const totals = this.calculateTotals(data);
            const today = new Date().toLocaleDateString('en-US', { 
                year: 'numeric', 
                month: 'long', 
                day: 'numeric' 
            });
            
            // Create HTML content optimized for Word conversion
            let html = '<!DOCTYPE html>' +
                '<html xmlns:o="urn:schemas-microsoft-com:office:office" xmlns:w="urn:schemas-microsoft-com:office:word" xmlns="http://www.w3.org/TR/REC-html40">' +
                '<head>' +
                '<meta charset="utf-8">' +
                '<meta name="ProgId" content="Word.Document">' +
                '<meta name="Generator" content="Microsoft Word 15">' +
                '<meta name="Originator" content="Microsoft Word 15">' +
                '<title>Expense Report - ' + today + '</title>' +
                '<style>' +
                '@page { size: 8.5in 11in; margin: 1in; }' +
                'body { font-family: "Calibri", "Arial", sans-serif; font-size: 11pt; line-height: 1.15; margin: 0; padding: 0; }' +
                'h1 { color: #2E7D32; text-align: center; font-size: 18pt; font-weight: bold; margin-bottom: 12pt; }' +
                'h2 { color: #2E7D32; font-size: 14pt; font-weight: bold; margin-top: 18pt; margin-bottom: 6pt; }' +
                'h3 { color: #2E7D32; font-size: 12pt; font-weight: bold; margin-top: 12pt; margin-bottom: 6pt; }' +
                'p { margin: 0 0 6pt 0; }' +
                'table { border-collapse: collapse; width: 100%; margin: 12pt 0; font-size: 10pt; }' +
                'th, td { border: 1pt solid #000000; padding: 3pt; text-align: left; vertical-align: top; }' +
                'th { background-color: #D9D9D9; font-weight: bold; text-align: center; }' +
                '.summary { background-color: #F2F2F2; padding: 9pt; margin: 12pt 0; border: 1pt solid #000000; }' +
                '.footer { text-align: center; color: #666666; font-style: italic; margin-top: 24pt; font-size: 9pt; }' +
                '.date { text-align: center; color: #666666; margin-bottom: 12pt; font-size: 10pt; }' +
                '.amount { text-align: right; }' +
                '</style>' +
                '</head>' +
                '<body>' +
                '<h1>Expense Report</h1>' +
                '<p class="date">Generated on ' + today + '</p>' +
                '<div class="summary">' +
                '<h3>Summary</h3>' +
                '<p><strong>Total Expenses:</strong> $' + totals.grandTotal.toFixed(2) + '</p>' +
                '<p><strong>Number of Records:</strong> ' + totals.totalInvoices + '</p>' +
                '</div>' +
                '<h2>Expense Details</h2>' +
                '<table>' +
                '<thead>' +
                '<tr>' +
                '<th>Invoice #</th>' +
                '<th>Date</th>' +
                '<th>Vendor</th>' +
                '<th>Amount</th>' +
                '<th>Tax</th>' +
                '<th>Total</th>' +
                '<th>Category</th>' +
                '</tr>' +
                '</thead>' +
                '<tbody>';
            
            data.forEach(invoice => {
                const totalAmount = (invoice.amount || 0) + (invoice.taxAmount || 0);
                html += '<tr>' +
                    '<td>' + (invoice.invoiceNumber || 'N/A') + '</td>' +
                    '<td>' + formatDate(invoice.date) + '</td>' +
                    '<td>' + (invoice.vendor || 'N/A') + '</td>' +
                    '<td class="amount">$' + (invoice.amount || 0).toFixed(2) + '</td>' +
                    '<td class="amount">$' + (invoice.taxAmount || 0).toFixed(2) + '</td>' +
                    '<td class="amount">$' + totalAmount.toFixed(2) + '</td>' +
                    '<td>' + (invoice.category || 'N/A') + '</td>' +
                    '</tr>';
            });
            
            html += '</tbody>' +
                '</table>' +
                '<div class="footer">Created with tidiful.com</div>' +
                '</body>' +
                '</html>';

            // Download as HTML file that can be opened in Word
            this.downloadFile(html, 'application/msword', 'expense_report_' + this.timestamp + '.doc');

        } catch (error) {
            console.error('DOCX Export Error:', error);
            alert('Error creating Word document. Please check the console for details.');
        }
    }

    /**
     * Export data as PDF
     * @param {Array} data - Array of invoice/expense objects
     * @param {Function} formatDate - Date formatting function
     */
    exportPDF(data, formatDate) {
        if (typeof window.jspdf === 'undefined' || typeof window.jspdf.jsPDF === 'undefined') {
            alert('PDF library not loaded. Please refresh the page and try again.');
            return;
        }

        try {
            const totals = this.calculateTotals(data);
            const today = new Date().toLocaleDateString('en-US', { 
                year: 'numeric', 
                month: 'long', 
                day: 'numeric' 
            });

            const { jsPDF } = window.jspdf;
            const doc = new jsPDF();

            // Title
            doc.setFontSize(20);
            doc.setTextColor(46, 125, 50); // Green color
            doc.text('Expense Report', 105, 20, { align: 'center' });

            // Date
            doc.setFontSize(12);
            doc.setTextColor(100, 100, 100);
            doc.text('Generated on ' + today, 105, 30, { align: 'center' });

            // Summary
            doc.setFontSize(14);
            doc.setTextColor(46, 125, 50);
            doc.text('Summary', 20, 50);

            doc.setFontSize(10);
            doc.setTextColor(0, 0, 0);
            doc.text('Total Expenses: $' + totals.grandTotal.toFixed(2), 20, 60);
            doc.text('Number of Records: ' + totals.totalInvoices, 20, 70);

            // Table
            doc.setFontSize(14);
            doc.setTextColor(46, 125, 50);
            doc.text('Expense Details', 20, 90);

            // Table headers
            const headers = ['Invoice #', 'Date', 'Vendor', 'Amount', 'Tax', 'Total', 'Category'];
            const colWidths = [25, 20, 35, 20, 15, 20, 25];
            let x = 20;
            
            doc.setFontSize(8);
            doc.setTextColor(0, 0, 0);
            headers.forEach((header, i) => {
                doc.text(header, x, 100);
                x += colWidths[i];
            });

            // Table data
            let y = 110;
            data.forEach((invoice, index) => {
                if (y > 280) { // New page if needed
                    doc.addPage();
                    y = 20;
                }
                
                const totalAmount = (invoice.amount || 0) + (invoice.taxAmount || 0);
                const rowData = [
                    invoice.invoiceNumber || 'N/A',
                    formatDate(invoice.date),
                    invoice.vendor || 'N/A',
                    '$' + (invoice.amount || 0).toFixed(2),
                    '$' + (invoice.taxAmount || 0).toFixed(2),
                    '$' + totalAmount.toFixed(2),
                    invoice.category || 'N/A'
                ];

                x = 20;
                rowData.forEach((cell, i) => {
                    doc.text(cell, x, y);
                    x += colWidths[i];
                });
                y += 8;
            });

            // Footer
            doc.setFontSize(8);
            doc.setTextColor(100, 100, 100);
            doc.text('Created with tidiful.com', 105, 290, { align: 'center' });

            // Download
            doc.save('expense_report_' + this.timestamp + '.pdf');

        } catch (error) {
            console.error('PDF Export Error:', error);
            alert('Error creating PDF document. Please check the console for details.');
        }
    }

    /**
     * Export data as QIF (Quicken Interchange Format)
     * @param {Array} data - Array of invoice/expense objects
     * @param {Function} formatDate - Date formatting function
     */
    exportQIF(data, formatDate) {
        let qifContent = '!Type:Bank\n';
        
        data.forEach(invoice => {
            const totalAmount = (invoice.amount || 0) + (invoice.taxAmount || 0);
            qifContent += 'D' + formatDate(invoice.date) + '\n';
            qifContent += 'T-' + totalAmount.toFixed(2) + '\n'; // Negative for expense
            qifContent += 'P' + (invoice.vendor || 'N/A') + '\n';
            qifContent += 'M' + (invoice.category || 'N/A') + '\n';
            qifContent += '^' + '\n'; // End of transaction
        });

        this.downloadFile(qifContent, 'text/plain;charset=utf-8', 'expenses_' + this.timestamp + '.qif');
    }

    /**
     * Export data as IIF (Intuit Interchange Format)
     * @param {Array} data - Array of invoice/expense objects
     * @param {Function} formatDate - Date formatting function
     */
    exportIIF(data, formatDate) {
        let iifContent = '!TRNS\tTRNSTYPE\tDATE\tACCNT\tNAME\tAMOUNT\tMEMO\n';
        iifContent += '!SPL\tSPLID\tTRNSTYPE\tDATE\tACCNT\tNAME\tAMOUNT\tMEMO\n';
        iifContent += '!ENDTRNS\n';
        
        data.forEach((invoice, index) => {
            const totalAmount = (invoice.amount || 0) + (invoice.taxAmount || 0);
            const date = formatDate(invoice.date).replace(/\//g, '');
            
            iifContent += 'TRNS\tGENERAL JOURNAL\t' + date + '\tExpenses\t' + 
                         (invoice.vendor || 'N/A') + '\t-' + totalAmount.toFixed(2) + 
                         '\t' + (invoice.category || 'N/A') + '\n';
            iifContent += 'SPL\t' + (index + 1) + '\tGENERAL JOURNAL\t' + date + 
                         '\tAccounts Payable\t' + (invoice.vendor || 'N/A') + '\t' + 
                         totalAmount.toFixed(2) + '\t' + (invoice.category || 'N/A') + '\n';
            iifContent += 'ENDTRNS\n';
        });

        this.downloadFile(iifContent, 'text/plain;charset=utf-8', 'expenses_' + this.timestamp + '.iif');
    }

    /**
     * Export data as XML
     * @param {Array} data - Array of invoice/expense objects
     * @param {Function} formatDate - Date formatting function
     */
    exportXML(data, formatDate) {
        const totals = this.calculateTotals(data);
        const today = new Date().toISOString();
        
        let xmlContent = '<?xml version="1.0" encoding="UTF-8"?>\n';
        xmlContent += '<expenseReport generated="' + today + '">\n';
        xmlContent += '  <summary>\n';
        xmlContent += '    <totalExpenses>' + totals.grandTotal.toFixed(2) + '</totalExpenses>\n';
        xmlContent += '    <totalRecords>' + totals.totalInvoices + '</totalRecords>\n';
        xmlContent += '  </summary>\n';
        xmlContent += '  <expenses>\n';
        
        data.forEach(invoice => {
            const totalAmount = (invoice.amount || 0) + (invoice.taxAmount || 0);
            xmlContent += '    <expense>\n';
            xmlContent += '      <invoiceNumber>' + (invoice.invoiceNumber || 'N/A') + '</invoiceNumber>\n';
            xmlContent += '      <date>' + formatDate(invoice.date) + '</date>\n';
            xmlContent += '      <vendor>' + (invoice.vendor || 'N/A') + '</vendor>\n';
            xmlContent += '      <amount>' + (invoice.amount || 0).toFixed(2) + '</amount>\n';
            xmlContent += '      <taxAmount>' + (invoice.taxAmount || 0).toFixed(2) + '</taxAmount>\n';
            xmlContent += '      <totalAmount>' + totalAmount.toFixed(2) + '</totalAmount>\n';
            xmlContent += '      <category>' + (invoice.category || 'N/A') + '</category>\n';
            xmlContent += '      <currency>' + (invoice.currency || 'USD') + '</currency>\n';
            xmlContent += '    </expense>\n';
        });
        
        xmlContent += '  </expenses>\n';
        xmlContent += '  <footer>Created with tidiful.com</footer>\n';
        xmlContent += '</expenseReport>';

        this.downloadFile(xmlContent, 'application/xml;charset=utf-8', 'expenses_' + this.timestamp + '.xml');
    }

    /**
     * Calculate totals from data
     * @param {Array} data - Array of invoice/expense objects
     * @returns {Object} Totals object
     */
    calculateTotals(data) {
        if (data.length === 0) {
            return {
                totalInvoices: 0,
                grandTotal: 0
            };
        }
        
        const grandTotal = data.reduce((sum, invoice) => {
            return sum + (invoice.amount || 0) + (invoice.taxAmount || 0);
        }, 0);
        
        return {
            totalInvoices: data.length,
            grandTotal: grandTotal
        };
    }

    /**
     * Download file using blob
     * @param {string} content - File content
     * @param {string} mimeType - MIME type
     * @param {string} filename - Filename
     */
    downloadFile(content, mimeType, filename) {
        const blob = new Blob([content], { type: mimeType });
        const url = window.URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = filename;
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);
        window.URL.revokeObjectURL(url);
    }
}

// Export dropdown management
class ExportDropdown {
    constructor() {
        this.dropdown = null;
        this.isInitialized = false;
    }

    /**
     * Initialize the export dropdown
     */
    init() {
        if (this.isInitialized) return;
        
        this.dropdown = document.getElementById('exportDropdown');
        if (!this.dropdown) {
            console.error('Export dropdown not found');
            return;
        }

        // Close dropdown when clicking outside
        document.addEventListener('click', (e) => {
            const button = e.target.closest('button[onclick="toggleExportDropdown()"]');
            if (!this.dropdown.contains(e.target) && !button) {
                this.hide();
            }
        });

        this.isInitialized = true;
    }

    /**
     * Toggle dropdown visibility
     */
    toggle() {
        if (!this.dropdown) return;
        this.dropdown.classList.toggle('hidden');
    }

    /**
     * Hide dropdown
     */
    hide() {
        if (!this.dropdown) return;
        this.dropdown.classList.add('hidden');
    }

    /**
     * Show dropdown
     */
    show() {
        if (!this.dropdown) return;
        this.dropdown.classList.remove('hidden');
    }
}

// Global instances
window.exportUtils = new ExportUtils();
window.exportDropdown = new ExportDropdown();

// Global functions for backward compatibility
window.toggleExportDropdown = function() {
    window.exportDropdown.toggle();
};

window.hideExportDropdown = function() {
    window.exportDropdown.hide();
};

window.exportData = function(format) {
    // Get current data from the datagrid
    const currentData = window.currentData || [];
    const formatDate = window.formatDate || function(date) { return date || 'N/A'; };
    
    window.exportUtils.exportData(currentData, format, formatDate);
    window.exportDropdown.hide();
};
