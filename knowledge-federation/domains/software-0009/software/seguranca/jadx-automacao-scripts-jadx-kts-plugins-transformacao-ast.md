---
id: software.seguranca.tranche10.000930
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

# JADX Scripting (**`.jadx.kts` Kotlin Scripts**) & `jadx plugins`: Automação de Desofuscação de Strings e Transformação da AST no Pipeline de Decompilação

## Em uma frase
Ofuscadores comerciais de Android (como DexGuard, Allatori, Stringer ou packers customizados de malware bancário) frequentemente escondem todas as strings literais do aplicativo substituindo `"https://api.c2.evil/..."` por uma chamada para uma função de descriptografia em runtime, como `StringDecryptor.decrypt(new byte[]{0x12, 0x4f, ...}, 0x5A)`!

## Por que importa
Se você olhar o código decompilado sem desofuscar essas chamadas, verá milhares de arrays de bytes ilegíveis em vez de URLs e chaves.

## Como funciona
A partir das versões modernas, o JADX possui suporte nativo a **Scripts em Kotlin (`.jadx.kts`)** e ao gerenciador **`jadx plugins`** (`jadx plugins --list`, `jadx plugins --install`): um script `.jadx.kts` passado diretamente na linha de comando junto com o `.apk` tem acesso completo à **API da Árvore Sintática Abstrata (AST) do JADX**, permitindo localizar chamadas para métodos de ofuscação, calcular a string descriptografada e **substituir o nó da AST pela string limpa antes que o JADX grave o arquivo `.java`**!

## Exemplo
```kotlin
// deobf_custom.jadx.kts — Exemplo de script Kotlin para o JADX que personaliza opcoes e inspeciona classes carregadas
val jadx = getJadxInstance()

jadx.stages.afterLoad {root ->
    log.info { "Total de classes carregadas no APK: ${root.classes.size}" }
    for (cls in root.classes) {
        if (cls.name.contains("Security") || cls.name.contains("Pinning") || cls.name.contains("Crypto")) {
            log.info { "[AUDIT TARGET] Classe sensivel localizada: ${cls.fullName}" }
        }
    }
}
```

## Limites e trade-offs
Você pode passar o script `.jadx.kts` tanto na CLI (**`jadx -d out app.apk deobf_custom.jadx.kts`**) quanto editá-lo e executá-lo ao vivo dentro do **`jadx-gui`** com realce de sintaxe e autocompletar!

## Como verificar
Explore os plugins disponíveis na comunidade executando `jadx plugins --available`.

## Conexões
- [[jadx-depurador-smali-integrado-jadx-gui-adb-jdwp-breakpoints]] — Veja também: JADX **`jadx-gui` Smali Debugger**: Depuração Passo a Passo via **JDWP / `adb`**, Inspeção de Registradores (`v0`, `p0`) e *Stack Frames* em Tempo Real.
- [[jadx-arquitetura-decompilador-dex-java-apk-aab-arsc-android]] — Referência cruzada direta com jadx-arquitetura-decompilador-dex-java-apk-aab-arsc-android.
- [[jadx-desofuscacao-automatica-deobf-mappings-proguard-r8-kotlin]] — Referência cruzada direta com jadx-desofuscacao-automatica-deobf-mappings-proguard-r8-kotlin.

## Fontes
- [JADX Official GitHub — Dex to Java Decompiler CLI & GUI Options Reference](https://raw.githubusercontent.com/skylot/jadx/master/README.md) — documentação oficial completa do JADX cobrindo opções de linha de comando, modos de decompilação, desofuscação, grafos CFG/Call-Graph e plugins Kotlin/mappings; consultado em 2026-10-03.
- [JADX Official Wiki — jadx-gui Features Overview & Security Analysis](https://github.com/skylot/jadx/wiki/jadx-gui-features-overview) — wiki oficial do JADX demonstrando navegação no AndroidManifest.xml, busca de referências, modo debug Smali e exclusão de pacotes; consultado em 2026-10-03.
