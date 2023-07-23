'''
Replaces default legend handle with a text handle.
'''

import matplotlib.text as mpl_text

class TextLegend():
    '''
    Container for text legend handle.
    
    Attributes
    ----------
    my_text : str
        Text of legend handle.
    color : str
        Color of legend handle.

    Parameters
    ----------
    text : str
        Text of legend handle.
    color : str
        Color of legend handle.
    '''
    # pylint: disable=too-few-public-methods
    # This class format is just for data storage

    def __init__(self, text, color):
        self.my_text = text
        self.my_color = color

class TextLegendHandler():
    '''
    Handler object for use in matplotlib when replacing default legend handle
    with a text based one.
    '''
    # pylint: disable=too-few-public-methods
    # This class format is required by Matplotlib

    def legend_artist(self, orig_handle, fontsize, handlebox):
        '''
        Create legend artist with text handle.

        Parameters
        ----------
        orig_handle : object
            Original handle of legend object.
        fontsize : float
            Size of font.
        handlebox : object
            Box in which handle is contained.
        '''
        patch = mpl_text.Text(x=0, y=0, text=orig_handle.my_text + " " + "\u2014",
                              color=orig_handle.my_color, verticalalignment='baseline',
                                horizontalalignment='left', multialignment=None,
                                fontproperties=None, linespacing=None,
                                rotation_mode=None, size=fontsize, family="Times New Roman")
        handlebox.add_artist(patch)
        return patch
