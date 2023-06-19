import matplotlib.text as mpl_text

class TextLegend(object):
    def __init__(self, text, color):
        self.my_text = text
        self.my_color = color

class TextLegendHandler(object):
    def legend_artist(self, legend, orig_handle, fontsize, handlebox):
    
        x0, y0 = handlebox.xdescent, handlebox.ydescent
        width, height = handlebox.width, handlebox.height
        patch = mpl_text.Text(x=0, y=0, text=orig_handle.my_text, color=orig_handle.my_color, verticalalignment=u'baseline', 
                                horizontalalignment=u'left', multialignment=None, 
                                fontproperties=None, linespacing=None, 
                                rotation_mode=None)
        handlebox.add_artist(patch)
        return patch