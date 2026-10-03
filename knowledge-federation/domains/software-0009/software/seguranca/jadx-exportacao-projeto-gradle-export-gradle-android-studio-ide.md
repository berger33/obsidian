---
id: software.seguranca.tranche10.000928
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

# JADX **`-e` / `--export-gradle`**: Exportação Direta do APK/AAR como um **Projeto Gradle (`build.gradle`)** para Análise no **Android Studio / IntelliJ IDEA**

## Em uma frase
Embora a interface gráfica `jadx-gui` seja excelente para navegação rápida, busca de referências (*Find Usage*) e renomeação, às vezes o auditor quer usar os recursos avançados de refatoração, inspeção de dataflow e plugins de SAST do **Android Studio** ou **IntelliJ IDEA** sobre o código decompilado.

## Por que importa
Para isso, a flag **`-e` (`--export-gradle`)** combinada com **`--export-gradle-type auto | android-app | android-library | simple-java`** faz o JADX organizar todos os arquivos `.java`, `AndroidManifest.xml`, `res/` e assets no layout oficial do Gradle e **gerar automaticamente os arquivos `build.gradle`, `settings.gradle` e dependências inferidas**!

## Como funciona
Basta abrir a pasta gerada no Android Studio / IntelliJ IDEA para navegar pelo código com indexação completa da IDE!

## Exemplo
```bash
# Exportar um APK decompilado diretamente como um projeto Gradle completo (-e / --export-gradle) pronto para abrir no Android Studio
jadx --export-gradle \
  --export-gradle-type android-app \
  --deobf \
  -d /cases/mobile/app_gradle_project \
  /cases/mobile/target_app.apk
```

## Limites e trade-offs
Quando você quiser apenas ler e auditar o código no IDE sem que erros de sintaxe em classes de bibliotecas de terceiros (`androidx.*`, `com.google.*`) atrapalhem a indexação, exclua os pacotes padrão de SDK no `jadx-gui` (*Package exclude* com clique direito na árvore de pacotes) antes de exportar!

## Como verificar
Observação técnica: para modificar um APK e recompilá-lo de volta em um `.apk` funcional (patching de recursos/bytecode), prefira usar o **Apktool (`apktool d` -> editar Smali/XML -> `apktool b`)** em vez de tentar recompilar o Java decompilado.

## Conexões
- [[jadx-exportacao-grafos-fluxo-controle-cfg-call-graph-dot-json]] — Veja também: JADX: Exportação de **Control Flow Graphs (`--cfg`, `--raw-cfg`)**, **Grafo de Chamadas (`--call-graph json|dot`)** e Saída Estruturada (`--output-format json`).
- [[jadx-depurador-smali-integrado-jadx-gui-adb-jdwp-breakpoints]] — Veja também: JADX **`jadx-gui` Smali Debugger**: Depuração Passo a Passo via **JDWP / `adb`**, Inspeção de Registradores (`v0`, `p0`) e *Stack Frames* em Tempo Real.
- [[jadx-arquitetura-decompilador-dex-java-apk-aab-arsc-android]] — Referência cruzada direta com jadx-arquitetura-decompilador-dex-java-apk-aab-arsc-android.
- [[apktool-recompilacao-build-use-aapt2-zipalign-apksigner-v2-v3]] — Referência cruzada direta com apktool-recompilacao-build-use-aapt2-zipalign-apksigner-v2-v3.
- [[jadx-desofuscacao-automatica-deobf-mappings-proguard-r8-kotlin]] — Referência cruzada direta com jadx-desofuscacao-automatica-deobf-mappings-proguard-r8-kotlin.

## Fontes
- [JADX Official GitHub — Dex to Java Decompiler CLI & GUI Options Reference](https://raw.githubusercontent.com/skylot/jadx/master/README.md) — documentação oficial completa do JADX cobrindo opções de linha de comando, modos de decompilação, desofuscação, grafos CFG/Call-Graph e plugins Kotlin/mappings; consultado em 2026-10-03.
- [JADX Official Wiki — jadx-gui Features Overview & Security Analysis](https://github.com/skylot/jadx/wiki/jadx-gui-features-overview) — wiki oficial do JADX demonstrando navegação no AndroidManifest.xml, busca de referências, modo debug Smali e exclusão de pacotes; consultado em 2026-10-03.
