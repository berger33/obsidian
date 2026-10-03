---
id: software.testes.tranche25.001896
tipo: tecnica
dominio: software
subdominio: testes
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-25.md"
fontes: ["https://raw.githubusercontent.com/diffblue/cbmc/develop/README.md", "https://github.com/diffblue/cbmc"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Instalação no macOS com Homebrew: upgrade automático, brew pin e tap histórico

## Em uma frase
Na subseção macOS, o README mostra a instalação pelo Homebrew/core com brew install cbmc (ou brew upgrade cbmc), alerta que o Homebrew atualiza fórmulas automaticamente para a última versão disponível — sugerindo brew pin cbmc para travar a versão caso você não queira upgrades involuntários — e aponta o tap mantido pelo projeto (github.com/diffblue/homebrew-cbmc, documentado em doc/ADR/homebrew_tap.md) para instalar versões históricas.

## Por que importa
Em verificação formal, uma mudança inesperada de versão do verificador durante um brew update geral na máquina do desenvolvedor pode alterar resultados ou flags em meio a uma auditoria; o brew pin cbmc e o tap de versões históricas garantem reprodutibilidade no macOS.

## Como funciona
Instale com brew install cbmc, execute brew pin cbmc se o seu projeto exigir versão fixa do verificador e recorra ao tap diffblue/homebrew-cbmc conforme doc/ADR/homebrew_tap.md quando precisar reproduzir resultados de uma versão anterior.

## Exemplo
Dois comandos no terminal do macOS — brew install cbmc seguido de brew pin cbmc — instalam a versão atual do Homebrew/core e impedem que atualizações futuras de outros pacotes troquem o binário do CBMC sem aviso.

## Limites e trade-offs
O comando brew pin trava apenas uma versão já instalada localmente; se você precisa instalar diretamente uma versão antiga que não está mais no Homebrew/core, o caminho correto é o homebrew tap mantido pela Diffblue.

## Como verificar
Conferi a subseção macOS da seção Installing no README oficial.

## Conexões
- [[cbmc-linux-install-abi-caveat]] — Veja também: Três caminhos de instalação no Linux e a ressalva de ABI da libc/libc++.
- [[cbmc-contributing-workflow-develop]] — Veja também: Fluxo de contribuição: branch a partir de develop e CODING_STANDARD.md.

## Fontes
- [CBMC — README oficial](https://raw.githubusercontent.com/diffblue/cbmc/develop/README.md) — README oficial do CBMC com suporte a C89–C23, extensões gcc/Visual Studio, SystemC/Scoot, Verilog, loop unwinding, canais release vs develop, instalação em Windows/Linux/macOS, contribuição e licença 4-clause BSD.; consultado em 2026-10-03.
- [Repositório oficial diffblue/cbmc](https://github.com/diffblue/cbmc) — Repositório oficial do CBMC e da suíte CProver no GitHub com releases, TOOLS_OVERVIEW.md, COMPILING.md, CODING_STANDARD.md e FEATURE_IDEAS.md.; consultado em 2026-10-03.
