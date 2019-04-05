
from gi import require_version
require_version( 'Gtk', '3.0' )
from gi.repository import Gtk
from gi.repository import Gdk
from gi.repository import Pango
from Calculator import  Calculator

class CalculatorViewer( Gtk.Window ):

    def __init__( self):
        super().__init__( title="Sumkowy Kalkulator", window_position = Gtk.WindowPosition.CENTER )
        self.set_default_size( 400, 300 )
        self.set_resizable(True)
        self.__calculator = Calculator()
        self.__equatation_label = Gtk.Label(self.__calculator.Display, halign = Gtk.Align.END)
        self.__icons = Gtk.DrawingArea()
        self.__buttonMatrix = self.createButtons()
        self.__memory_visible = False
        self.__minus_visible = False
        self.__error_visible = False
        self.__menubar = Gtk.MenuBar()

        acgroup = Gtk.AccelGroup()
        self.add_accel_group(acgroup)

        menu1 = Gtk.Menu()
        file = Gtk.MenuItem("Plik")
        item1 = Gtk.MenuItem("Wyjście")
        item1.add_accelerator("activate", acgroup, ord('Q'), Gdk.ModifierType.CONTROL_MASK, Gtk.AccelFlags.VISIBLE)
        item1.connect('activate', self.exit)
        file.set_submenu(menu1)
        menu1.append(item1)
        self.__menubar.append(file)

        self.connect('check-resize', self.resizeEvent)

        self.__icons.connect("draw",self.paint)
        self.__icons.set_size_request(30,80)

        b1 = Gtk.Box(orientation= Gtk.Orientation.VERTICAL)
        b1.pack_start(self.__menubar, False, False,0)
        screen = Gtk.Box(orientation= Gtk.Orientation.HORIZONTAL)
        screen.pack_start(self.__icons, False, True, 0)
        screen.pack_start(self.__equatation_label, True, True, 0)

        b1.pack_start(screen, True, True, 0)
        buttonLayout = Gtk.Grid()

        row_idx = 0;
        for button_row in self.__buttonMatrix:
            col_idx = 0
            for [button, rowspan, colspan] in button_row:
                buttonLayout.attach(button, col_idx, row_idx, colspan, rowspan)
                col_idx += colspan
            row_idx += 1
        b1.pack_start(buttonLayout, False, True, 0)
        self.add(b1)

    def exit(self, a):
        exit()

    def createButtons(self):

        buttons = [

            [
                self.createButton("C/CE", colspan=2),
                self.createButton("\u221A"),
                self.createButton("\u0025")
            ],
            [
                self.createButton("MRC"),
                self.createButton("M-"),
                self.createButton("M+"),
                self.createButton("\u00F7")
            ],
            [
                self.createButton("7"),
                self.createButton("8"),
                self.createButton("9"),
                self.createButton("x")
            ],
            [
                self.createButton("4"),
                self.createButton("5"),
                self.createButton("6"),
                self.createButton("-")
            ],
            [
                self.createButton("1"),
                self.createButton("2"),
                self.createButton("3"),
                self.createButton("+", rowspan=2),
            ],
            [
                self.createButton("0"),
                self.createButton("."),
                self.createButton("="),
            ]
        ]
        return buttons

    def createButton(self,char, rowspan = 1, colspan=1):
        button = Gtk.Button(char)
        button.connect("clicked", self.make_calluser(char))
        button.set_hexpand(True)
        button.set_vexpand(True)
        return [button,rowspan,colspan]

    def make_calluser(self, name):
        if name == "\u00F7":
            name = "/"
        elif name == "\u0025":
            name = "p"
        elif name == "\u221A":
            name = "sqrt"

        def calluser(button):
            self.__calculator.Press(name)
            self.__equatation_label.set_text(self.__calculator.Display)
            self.__minus_visible = self.__calculator.IsNegative
            self.__error_visible = self.__calculator.Error
            self.__memory_visible = self.__calculator.IsMemorized
            self.queue_draw()
        return calluser

    def paint( self, widget, context ):
        w, h = self.__icons.get_allocated_width(), self.__icons.get_allocated_height()

        middle = h / 2

        context.set_source_rgb(0, 0, 0)

        memory_h_mid = middle - middle / 2
        memory_w_mid = w / 2
        memory_w_lSlash = memory_w_mid / 2
        memory_w_rSlash = memory_w_mid + memory_w_mid / 2
        memory_h_Slash_start = memory_h_mid + memory_h_mid - 10
        memory_h_Slash_end = 10

        if self.__memory_visible:
            context.move_to(memory_w_lSlash, memory_h_Slash_start)
            context.line_to(memory_w_lSlash, memory_h_Slash_end)
            context.line_to(memory_w_mid, memory_h_mid)
            context.line_to(memory_w_rSlash, memory_h_Slash_end)
            context.line_to(memory_w_rSlash, memory_h_Slash_start)
            context.stroke()

        minus_h = middle
        minus_w_start = 5
        minus_w_end = w - 5

        if self.__minus_visible:
            context.move_to(minus_w_start, minus_h)
            context.line_to(minus_w_end, minus_h)
            context.stroke()

        error_h_mid = middle + middle / 2
        error_w_mid = 5
        error_h_lShlash_start = middle + 10
        error_h_lShlash_end = h - 10
        error_longer_end = w - 5
        error_mid_end = w / 2

        if self.__error_visible:
            context.move_to(error_w_mid, error_h_lShlash_start)
            context.line_to(error_w_mid, error_h_lShlash_end)

            context.move_to(error_w_mid, error_h_lShlash_start)
            context.line_to(error_longer_end, error_h_lShlash_start)

            context.move_to(error_w_mid, error_h_lShlash_end)
            context.line_to(error_longer_end, error_h_lShlash_end)

            context.move_to(error_w_mid, error_h_mid)
            context.line_to(error_mid_end, error_h_mid)

            context.stroke()

    def resizeEvent(self, window):
        if self.get_allocated_height() < 300 or self.get_allocated_width() < 400:
            self.set_size_request(400, 300)
            return None
        fontSize = self.get_allocated_height() * 0.1
        if fontSize != 0:
            font = Pango.FontDescription("Times Bold {}".format(int(fontSize)))
            self.__equatation_label.modify_font(font)
        value = self.get_allocated_width() * 0.1
        self.__icons.set_size_request(value,80)



w = CalculatorViewer()
w.connect("delete-event", Gtk.main_quit)
w.show_all()
Gtk.main()