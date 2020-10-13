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

    if (btn_mysql.className.indexOf('buttonChosen')!=-1) {
        btn_mysql.className = 'choiceButton';
        btn_redshift.className = 'choiceButton buttonChosen';
    }
}

function querySubmit() {
    var btn_mysql = document.getElementById('mysql');
    var form = document.getElementById('inputForm')

    if (btn_mysql.className.indexOf('buttonChosen')!=-1) {
        form.action = 'mysql';
    } else {
        form.action = 'redshift';
    }

    form.submit();
}