# Shiwake_Viewer

仕分けViewer


for Windows (Win11でのみ動作確認)


機能紹介


●ビューア機能

表示フォルダを指定してその中の画像・動画を閲覧できます。

画像:jpg, jpeg, gif, png, bmp, webpを表示可能。動画:mp4, webm, gifアニメ, webpアニメを再生可能。

(動画再生はAI生成物の確認用、i2iやloraの素材収集用で再生速度は正確ではありませんし音声も出ません。

鑑賞の場合はAPPsから動画再生ソフトを起動して下さい。)

動画は画面を一時停止してキャプチャ画像を保存することができます。(一部のmp4は再生できません)


●チェック機能

見ている画像や動画にチェックを付けてそのファイルの表示をスキップすることができます。

フォルダに削除するファイルの方が圧倒的に多い場合などは残す画像だけチェックで選んで別のフォルダに移動したり

チェックしていない画像をまとめて削除したりできます。

●仕分け機能

複数の行先フォルダを登録しワンクリックで閲覧中メディアを移動・コピーできます。

●アンドゥ機能

移動・コピー・削除の履歴からファイル操作をアンドゥできます

●アプリ起動機能

アプリケーションソフトのパスを登録しておき閲覧中メディアをアプリに送って起動出来ます。

拡張子ごとのデフォルトアプリに送ることもできます。

●メタデータ表示機能

A1111形式、NAI形式のメタデータを記録している画像はそのデータを表示・コピーすることができます。

●スライドショー機能

仕分け先として登録されているフォルダをPC内のmp3ファイルをBGMにしてスライドショー再生ができます。

データを登録してテキスト・ボイス付きで再生することもできます。(静止画のみ対応)



＜実行前に一読をお願いします＞

◯exe形式なので実行前にダウンロードしたファイルのセキュリティスキャンをお願いします。

私に悪意が無くても悪意のある人間にアカウントのパスワードを知られてファイルがすり替えられることもあります。

◯デフォルトでは削除したファイルは一旦削除フォルダに移動して後でまとめてごみ箱に送る設定になっています。

直接ごみ箱に送るように変更出来ますがその場合ファイル削除の操作履歴は残らずこのソフトでのアンドゥはできません。

◯正常に動作しなくなった場合

仕分けViewer.exeと同じフォルダに自動的に作られる設定ファイルのconfig.txtが原因の可能性があります。

一旦config.txtを別フォルダに移すなどして動作を試して下さい。手をかけてカスタムした設定のconfig.txtはコピーしておくことをおすすめします。




◎基本操作

画像・動画を閲覧する「表示フォルダ」の選択

　  ○「表示フォルダ」ボタンを押してフォルダを選択

　  ○エクスプローラーのフォルダ・画像を

  　 画像表示エリアにドラッグ・アンド・ドロップ

  　○Destフォルダのフレーム内をクリックする

　  ○起動中に一度閲覧したフォルダはフォルダ名が表示されている最上段のフレーム内でマウスホイールを上下することで再び選ぶことが出来ます

閲覧画像の選択

　　○画像をクリックで次の画像

　　○◀　▶ボタン(設定で移動量を変えられます)

　　○マウスホイールの上下

Destフォルダ（行先フォルダ・Destはdestinationの略）の選択

　　○「Destフォルダ」ボタンを押してフォルダを選択

　　○「Destフォルダ」ボタン右クリックで表示フォルダをDestフォルダに選ぶことができます。

　　○エクスプローラーのフォルダ・画像をDestフォルダのフレーム内にドラッグ・アンド・ドロップ

表示中の画像・動画ファイルを移動

　　対応するDestフォルダのフォルダ名のボタンをクリック

表示中の画像・動画ファイルをコピー

　　対応するDestフォルダのフォルダ名のボタンを右クリック

表示中の画像・動画ファイルを削除

　　「削除」ボタンをクリックして一時的に削除フォルダに移動（削除ボタン右クリックで削除フォルダに溜まったファイルをまとめてごみ箱に送れます。）

フォルダの内容をエクスプローラーで表示する

　　対応するフォルダの「Exp」ボタンを押す（「Exp」ボタン右クリックで簡単なファイル操作のメニューが出ます）

画像にチェックをつける

　　☑ボタン（チェックを付けた画像は同じ表示フォルダの選択中は表示されなくなります）

フォルダのチェック状況をセーブする

　　Save☑ボタン（移動元フォルダにcheck.txtを作りそこに保存します。同じフォルダを移動元フォルダに選んだ時チェック状況を自動ロードします。）

フォルダのチェック状況をリセットする

　　Reset☑ボタン（check.txtの削除もここで行えます）

表示中のファイル・フォルダを登録したアプリに送って起動

　　「APPsボタン」をクリックして対応するアプリを選択
  
　　「APPsボタン」を右クリックで拡張子別のデフォルトアプリに送って起動

メタデータ表示

　　Meta-dataボタンを押す
  
　　下段のボタンでプロンプトのコピー、表示形式変更
  
動画のコントロール

　　動画の再生/一時停止切り換え：「Stop/Play」ボタン
  
　　動画の後方・前方シーク：　シークバーをクリックで大まかな位置を選べます
  
　　　　◀・▶ボタンクリックで全体の⅛、右クリックで全体の1/64ずつ後退・前進
    
　　　　マウスホイール上下で１フレームずつ後退・前進
    
　　表示中フレームのキャプチャ：　CAPボタン
  
　　（設定からキャプチャ画像の保存先を選べます）

全画面モード

　　画像の上で右クリック
  
　　(全画面モード中はクリックで次画像、マウスホイールで画面スクロール、右クリック・ESCキーで全画面モード終了)

スライドショー

　　対応する行先フォルダのSlideボタンで起動

    クリックで設定画面
   
　　右クリックで画像の表示切替え
  
　　（スクロール表示、全画面表示、枠内固定表示）
  
　　ホイール上下：音量調節

アンドゥ

　　Undoボタンでウィンドウを開く
  
　　◀　▶ボタンでファイルを選択し移動・コピー・削除の対応するボタンでアンドゥ実行

表示順切替

　　表示ファイル名が書かれたフレーム右クリックでファイルの表示順を選ぶ事ができます。(名前順、作成日時順)
  
　　また表示フォルダ情報を一定間隔で更新してフォルダ内の最も新しい画像より後に作られた画像を
  
　　一定間隔でチェックして知らせることもできます。(フォルダチェックモード。表示順は作成日時順のみ)

データ表示ラベル切替

　　右下のファイルのデータ表示部分右クリックでデータ表示を動画用に切替える事ができます。
  


◎注意

現在実行中に突然プログラムが落ちる問題を確認しています。原因はスライドショーの音楽再生と思われます。

おまけ要素が原因で本筋の作業が中断しては本末転倒ですのでお手数ですが改善されるまでは

集中して画像整理をされる方は音楽を切って作業をされてください。

Comfy UIでtaggerやメタデータを使った画像仕分けを行うワークフローも併用すると効率が上がると思います。

https://huggingface.co/datasets/Gazou-Seiri-Bu/Picture-Sorting-Workflow/tree/main
