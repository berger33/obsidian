---
id: software.seguranca.tranche10.000929
tipo: tecnica
dominio: software
subdominio: seguranca
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-03
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-03
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-10.md"
fontes: ["https://raw.githubusercontent.com/skylot/jadx/master/README.md", "https://github.com/skylot/jadx/wiki/jadx-gui-features-overview"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# JADX **`jadx-gui` Smali Debugger**: Depuração Passo a Passo via **JDWP / `adb`**, Inspeção de Registradores (`v0`, `p0`) e *Stack Frames* em Tempo Real

## Em uma frase
Poucos analistas sabem que a interface gráfica **`jadx-gui`** inclui um **Depurador Dinâmico Smali/JDWP Integrado** (*Smali Debugger*)!

## Por que importa
Enquanto a janela principal do `jadx-gui` mostra o código Java reconstruído, você pode alternar para a visualização **Smali** (com `--add-debug-lines`), colocar **Breakpoints (`F9`)** em qualquer instrução, conectar o `jadx-gui` a um emulador Android ou celular físico via **`adb` (protocolo JDWP — *Java Debug Wire Protocol*)** e depurar o aplicativo linha por linha em execução!

## Como funciona
Sempre que a execução para em um breakpoint no `jadx-gui`, o painel de depuração exibe o valor em tempo real de todos os **registradores Dalvik locais (`v0`, `v1`, ...) e de parâmetros (`p0`, `p1`, ...)**, os campos do objeto `this` e a pilha de chamadas (*Call Stack*), permitindo inclusive **modificar o valor de um registrador na memória antes de continuar a execução (`F8` / `F7`)**!

## Exemplo
```bash
# Preparar o encaminhamento JDWP via adb listando os processos depuraveis no dispositivo e abrindo o APK no jadx-gui
adb devices
adb jdwp
# Na estacao de analise, iniciar o jadx-gui alocando 8 GB de heap JVM para APKs grandes:
JAVA_OPTS="-Xmx8G" jadx-gui /cases/mobile/target_app.apk
```

## Limites e trade-offs
E se o aplicativo de produção tiver `android:debuggable="false"` no `AndroidManifest.xml`, impedindo a conexão do depurador JDWP em um aparelho não-roteado? Você tem duas opções: **(1)** usar um emulador/dispositivo de laboratório com `ro.debuggable=1` (via Magisk `resetprop ro.debuggable 1`), ou **(2)** usar o **Apktool** para adicionar `android:debuggable="true"` no `AndroidManifest.xml`, recompilar (`apktool b`) e re-assinar o APK!

## Como verificar
Defina sempre `JAVA_OPTS="-Xmx8G"` ao abrir APKs grandes no `jadx-gui` para evitar lentidão de Garbage Collection durante a indexação de busca de texto completo.

## Conexões
- [[jadx-exportacao-projeto-gradle-export-gradle-android-studio-ide]] — Veja também: JADX **`-e` / `--export-gradle`**: Exportação Direta do APK/AAR como um **Projeto Gradle (`build.gradle`)** para Análise no **Android Studio / IntelliJ IDEA**.
- [[jadx-automacao-scripts-jadx-kts-plugins-transformacao-ast]] — Veja também: JADX Scripting (**`.jadx.kts` Kotlin Scripts**) & `jadx plugins`: Automação de Desofuscação de Strings e Transformação da AST no Pipeline de Decompilação.
- [[jadx-arquitetura-decompilador-dex-java-apk-aab-arsc-android]] — Referência cruzada direta com jadx-arquitetura-decompilador-dex-java-apk-aab-arsc-android.
- [[apktool-modificacao-androidmanifest-debuggable-network-security-config]] — Referência cruzada direta com apktool-modificacao-androidmanifest-debuggable-network-security-config.

## Fontes
- [JADX Official GitHub — Dex to Java Decompiler CLI & GUI Options Reference](https://raw.githubusercontent.com/skylot/jadx/master/README.md) — documentação oficial completa do JADX cobrindo opções de linha de comando, modos de decompilação, desofuscação, grafos CFG/Call-Graph e plugins Kotlin/mappings; consultado em 2026-10-03.
- [JADX Official Wiki — jadx-gui Features Overview & Security Analysis](https://github.com/skylot/jadx/wiki/jadx-gui-features-overview) — wiki oficial do JADX demonstrando navegação no AndroidManifest.xml, busca de referências, modo debug Smali e exclusão de pacotes; consultado em 2026-10-03.
