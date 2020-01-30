var BaseProcessor = require('BaseProcessor');
var build = require('RollupBaseBuild');

var VuePlugin = require('rollup-plugin-vue');
var plugins = [ VuePlugin() ];

class VueProcessor extends BaseProcessor {

    processResource(input, output, includeDependencies, excludeDependencies) {
        if(input && output) {
            return build(this.isProductionMode, input, output, includeDependencies, excludeDependencies, plugins);
        } else {
            throw new ReferenceError('input, output parameters are require to process the file', input);
        }
    }

    renderResource(render_file, context, i18n) {
        throw new ReferenceError('NOT SUPPORTED');
    }

}

module.exports = VueProcessor;