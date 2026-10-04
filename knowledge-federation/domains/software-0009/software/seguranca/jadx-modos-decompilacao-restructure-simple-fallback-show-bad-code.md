---
id: software.seguranca.tranche10.000922
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

# JADX: Modos de Decompilação (**`-m auto | restructure | simple | fallback`**) e **`--show-bad-code`** para Métodos Ofuscados que Falham no AST

## Em uma frase
Conforme alerta o `README.md` oficial do JADX, devido a otimizações agressivas do compilador **R8/D8** ou ofuscadores comerciais que criam grafos de fluxo de controle (*Control Flow Graphs*) irredutíveis ou blocos `try/catch` sobrepostos no bytecode Dalvik, em alguns métodos complexos o reconstrutor estruturado de Java pode falhar e exibir o comentário `/* JADX ERROR: Method code generation error */`.

## Por que importa
Para garantir que o auditor de segurança **nunca fique sem conseguir ler a lógica de um método crítico (como a rotina de criptografia ou Pinning TLS)**, o JADX oferece quatro modos de decompilação na flag **`-m` / `--decompilation-mode`** combinados com **`--show-bad-code`**!

## Como funciona
Os modos são: **`auto`** (tenta a melhor opção automaticamente, padrão), **`restructure`** (restaura estruturas completas `if/else/for/while/try`), **`simple`** (gera instruções Java lineares simplificadas com `goto` quando os loops estão corrompidos) e **`fallback`** (imprime as instruções brutas Dalvik sem tentar reconstruir blocos); enquanto **`--show-bad-code`** força o JADX a imprimir o código Java mesmo quando a verificação de consistência de tipos/registradores falhou parcialmente!

## Exemplo
```bash
# Decompilar uma unica classe critica (--single-class) que apresentou erro usando o modo simple e --show-bad-code
jadx --single-class "com.empresa.app.security.CryptoManager" \
  --single-class-output /cases/mobile/CryptoManager_simple.java \
  --decompilation-mode simple \
  --show-bad-code \
  --add-debug-lines \
  /cases/mobile/target_app.apk
```

## Limites e trade-offs
Observe a flag **`--single-class <nome_completo>`**: quando um APK gigante com 80.000 classes leva minutos para decompilar por inteiro, `--single-class` re-decompila **apenas aquela única classe em menos de 1 segundo**, permitindo testar rapidamente `--decompilation-mode simple` ou `--no-inline-methods`!

## Como verificar
Na interface gráfica `jadx-gui`, você também pode alternar instantaneamente qualquer classe entre as abas **Java**, **Simple** e **Smali** na parte inferior do editor.

## Conexões
- [[jadx-arquitetura-decompilador-dex-java-apk-aab-arsc-android]] — Veja também: **JADX (`skylot/jadx`)**: Arquitetura do Decompilador **Dalvik/ART Bytecode (`.dex`) para Java** e Decodificador Nativo de `.apk`, `.aab` e `resources.arsc`.
- [[jadx-desofuscacao-automatica-deobf-mappings-proguard-r8-kotlin]] — Veja também: JADX: Desofuscação Automática (**`--deobf`**, `.jobf`), Importação de Mapas **ProGuard/R8 (`--mappings-path`)** e Metadados **Kotlin (`kotlin.Metadata`)**.

## Fontes
- [JADX Official GitHub — Dex to Java Decompiler CLI & GUI Options Reference](https://raw.githubusercontent.com/skylot/jadx/master/README.md) — documentação oficial completa do JADX cobrindo opções de linha de comando, modos de decompilação, desofuscação, grafos CFG/Call-Graph e plugins Kotlin/mappings; consultado em 2026-10-03.
- [JADX Official Wiki — jadx-gui Features Overview & Security Analysis](https://github.com/skylot/jadx/wiki/jadx-gui-features-overview) — wiki oficial do JADX demonstrando navegação no AndroidManifest.xml, busca de referências, modo debug Smali e exclusão de pacotes; consultado em 2026-10-03.
