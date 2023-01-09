#Kivyのインターフェースを作成 → ボタンを配置する
#Kivyは基本的にOOPで書く
from kivy import Config

# a fixed size is set for the app's display when executed
Config.set("graphics", "height", "1000")
Config.set("graphics", "width", "600")

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stacklayout import StackLayout
from kivy.properties import StringProperty, NumericProperty

#日本語入力する為のフォントを追加する　　　　　　　
from kivy.core.text import LabelBase, DEFAULT_FONT  # 追加分
from kivy.resources import resource_add_path  # 追加分
resource_add_path('c:/Windows/Fonts')  # 追加分
LabelBase.register(DEFAULT_FONT, 'msgothic.ttc')  # 追加分

#ビルドに必要なパッケージ
from kivy.lang import Builder


#ボックスレイアウトのアプリを制作する練習を行う
class Game(BoxLayout):
    #ルート変数
    fontsize_h1 = "60dp"
    fontsize_h2 = "30dp"

    #グローバルで使える変数にするには、まず初期化する段階で宣言する必要がある。
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.Max_amount = 8
        self.Answer_done = False

        self.Eopenness = 0
        self.Econscient = 0
        self.Eextravers = 0
        self.Eagreeable = 0
        self.Eneurotic = 0

        self.Eopenness_per = 0
        self.Econscient_per = 0
        self.Eextravers_per = 0
        self.Eagreeable_per = 0
        self.Eneurotic_per = 0

        #プログレスバーの値
        self.PB_Eopenness = NumericProperty()
        self.PB_Conscient = NumericProperty()
        self.PB_EExtravers = NumericProperty()
        self.PB_EAgreeable = NumericProperty()
        self.PB_ENeurotic = NumericProperty()



    #画面を遷移
    def screen_transition_btn(self, sm, transto):

        if transto == "screen_default":
            #初期画面に行く場合、すべての値とスライダーの値を初期化する
            #グローバル変数をリセット
            self.Eopenness = 0
            self.Econscient = 0
            self.Eextravers = 0
            self.Eagreeable = 0
            self.Eneurotic = 0

            self.Eopenness_per = 0
            self.Econscient_per = 0
            self.Eextravers_per = 0
            self.Eagreeable_per = 0
            self.Eneurotic_per = 0

            self.PB_Eopenness = 0
            self.PB_Conscient = 0
            self.PB_EExtravers = 0
            self.PB_EAgreeable = 0
            self.PB_ENeurotic = 0

            #Kivy側のウィジェットをリセット
            self.ids.openness_per.text = str(0) + "%"
            self.ids.openness_PB.value = 0
            self.ids.conscient_per.text = str(0) + "%"
            self.ids.conscient_PB.value = 0
            self.ids.extravers_per.text = str(0) + "%"
            self.ids.extravers_PB.value = 0
            self.ids.agreeable_per.text = str(0) + "%"
            self.ids.agreeable_PB.value = 0
            self.ids.neurotic_per.text = str(0) + "%"
            self.ids.neurotic_PB.value = 0

        if transto == "screen_explanation" or sm.current == "screen_result02":
        # 説明画面に行く場合・回答が終了した場合のみ左側に遷移する
            sm.transition.direction = "right"
        else:
            sm.transition.direction = "left"
        sm.current = transto

    #画面を遷移 + 質問に答えて値を加算する
    def screen_answer_btn(self, sm, transto, element, amount):
        #因子に値を加算
        if element == "openness":
            self.Eopenness += amount
        if element == "conscient":
            self.Econscient += amount
        if element == "extravers":
            self.Eextravers += amount
        if element == "agreeable":
            self.Eagreeable += amount
        if element == "neurotic":
            self.Eneurotic += amount

        # スライダーの値をセットし直す。screen_answer_btnが実行されるたびに実行する
        self.PB_Eopenness = (self.Eopenness / self.Max_amount) * 100
        self.ids.openness_per.text = str((self.Eopenness / self.Max_amount) * 100) + "%"
        self.ids.openness_PB.value = self.PB_Eopenness

        self.PB_Econscient = (self.Econscient / self.Max_amount) * 100
        self.ids.conscient_per.text = str((self.Econscient / self.Max_amount) * 100) + "%"
        self.ids.conscient_PB.value = self.PB_Econscient

        self.PB_Eextravers = (self.Eextravers/ self.Max_amount) * 100
        self.ids.extravers_per.text = str((self.Eextravers/ self.Max_amount) * 100) + "%"
        self.ids.extravers_PB.value = self.PB_Eextravers

        self.PB_Eagreeable = (self.Eagreeable / self.Max_amount) * 100
        self.ids.agreeable_per.text = str((self.Eagreeable / self.Max_amount) * 100) + "%"
        self.ids.agreeable_PB.value = self.PB_Eagreeable

        self.PB_Eneurotic = (self.Eneurotic / self.Max_amount) * 100
        self.ids.neurotic_per.text = str((self.Eneurotic / self.Max_amount) * 100) + "%"
        self.ids.neurotic_PB.value = self.PB_Eneurotic

        #画面遷移
        if transto == "screen_explanation":
            sm.transition.direction = "right"
        else:
            sm.transition.direction = "left"
        sm.current = transto




"""
#スクロールビューの中にスタックレイアウトのボタンを配置できるようにする
class Buttons(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

"""

#アプリケーションのクラス
class TestApp(App):
    pass

#アプリケーションのクラスをインスタンシエート・実行する
TestApp().run()