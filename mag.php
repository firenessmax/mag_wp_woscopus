<?php
/*
Plugin Name: mag
*/
function get_papers_func( $atts ){

	$a = shortcode_atts(array(
		'auid' => 'something',
		'bar' => 'something else',
		'ggg' => 'asfdagadg'
	), $atts );

	$output = shell_exec(esc_attr(get_option('python_path','/bin/python')).' \''.substr(__FILE__, 0,-7).'main.py\' -g '.$a['auid']);
	return "<h3>Publicaciones</h3>".$output;
}
add_shortcode( 'get_papers', 'get_papers_func' );
?>

<?php
// create custom plugin settings menu
add_action('admin_menu', 'woscopus_tracker_create_menu');
add_action('sync_woscopus', 'woscopus_tracker_sync');

function woscopus_tracker_create_menu() {
	//create new top-level menu
	add_menu_page(
		'Woscopus Tracker', 
		'Woscopus Settings', 
		'manage_options', 
		"woscopus-options", 
		'woscopus_tracker_settings_page' 
	    );
	//call register settings function
    /*add_menu_page('Theme page title',
    	'Theme menu label', 
    	'manage_options',
    	'theme-options',
    	'wps_theme_func');*/
    add_submenu_page(
    	'woscopus-options',
    	'Actualización de datos',
    	'Woscopus Sync',
    	'manage_options',
    	'theme-op-faq',
    	'wps_theme_func_faq');


	add_action( 'admin_init', 'register_woscopus_tracker_settings' );
}

function wps_theme_func_faq(){
	?>
	<h1>Actualización WOS/Scopus ok</h1>
	<?php
	do_action('sync_woscopus'); 
	echo shell_exec(esc_attr(get_option('python_path','/bin/python')).' \''.substr(__FILE__, 0,-7).'main.py\' -s 0');
}

function register_woscopus_tracker_settings() {
	//register our settings
	register_setting( 'woscopus_tracker-settings-group', 'python_path' );
	register_setting( 'woscopus_tracker-settings-group', 'scopus_api_key' );
}


function woscopus_tracker_settings_page(){
?>
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

<a class="button button-primary" href="admin.php?page=theme-op-faq">sync</a>
<?php
}
