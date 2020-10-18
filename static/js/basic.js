function handleMysqlButtonClick(){
    var btn_mysql = document.getElementById('mysql');
    var btn_redshift = document.getElementById('redshift');

    if (btn_mysql.className.indexOf('buttonChosen')==-1) {
        btn_mysql.className = 'choiceButton buttonChosen';
        btn_redshift.className = 'choiceButton';
    }
}

function handleRedshiftButtonClick(){
    var btn_mysql = document.getElementById('mysql');
    var btn_redshift = document.getElementById('redshift');

    if (btn_redshift.className.indexOf('buttonChosen')==-1) {
        btn_mysql.className = 'choiceButton';
        btn_redshift.className = 'choiceButton buttonChosen';
    }
}

function handleInstacartButtonClick(){
    var instacart = document.getElementById('instacart');
    var abc_retail = document.getElementById('abc_retail');

    if (instacart.className.indexOf('buttonChosen')==-1) {
        instacart.className = 'choiceButton buttonChosen';
        abc_retail.className = 'choiceButton';
    }
}

function handleABCRetailButtonClick(){
    var instacart = document.getElementById('instacart');
    var abc_retail = document.getElementById('abc_retail');

    if (abc_retail.className.indexOf('buttonChosen')==-1) {
        abc_retail.className = 'choiceButton buttonChosen';
        instacart.className = 'choiceButton';
    }
}

function querySubmit() {
    var btn_mysql = document.getElementById('mysql');
    var instacart = document.getElementById('instacart');
    var form = document.getElementById('inputForm');

    if (btn_mysql.className.indexOf('buttonChosen')!=-1) {
        if (instacart.className.indexOf('buttonChosen')!=-1) {
            form.action = '/mysql/instacart';
        } else {
            form.action = '/mysql/abc_retail';
        }
    } else {
        if (instacart.className.indexOf('buttonChosen')!=-1) {
            form.action = '/redshift/instacart';
        } else {
            form.action = '/redshift/abc_retail';
        }
    }

    form.submit();
}