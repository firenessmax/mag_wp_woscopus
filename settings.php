<div class="wrap">
<h1>Seguimiento autores WOS/Scopus</h1>
<form method="post" action="options.php"
    <?php settings_fields( 'woscopus_tracker-settings-group' ); ?>
    <?php do_settings_sections( 'woscopus_tracker-settings-group' ); ?>
    <table class="form-table">
        <tr valign="top">
        <th scope="row">Python Path</th>
        <td><input type="text" name="python_path" value="<?php echo esc_attr( get_option('python_path') ); ?>" /></td>
        </tr>
        <tr valign="top">
        <th scope="row">Scopus API key</th>
        <td><input type="text" name="scopus_api_key" value="<?php echo esc_attr( get_option('scopus_api_key') ); ?>" /></td>
        </tr>
    </table>
    <?php submit_button(); ?>
</form>
</div> 