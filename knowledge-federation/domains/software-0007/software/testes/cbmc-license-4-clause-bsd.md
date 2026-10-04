---
id: software.testes.tranche25.001899
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

# Licenciamento sob 4-clause BSD license

## Em uma frase
A seção License do README oficial é direta: o CBMC é distribuído sob a "4-clause BSD license, see LICENSE file".

## Por que importa
Diferentemente das licenças BSD modernas de 2 ou 3 cláusulas, a licença BSD original de 4 cláusulas inclui a chamada cláusula de publicidade (advertising clause), um detalhe jurídico relevante que equipes de compliance de código aberto sempre verificam ao redistribuir ferramentas ou integrar código.

## Como funciona
Ao incluir o CBMC em distribuições internas, imagens de contêiner redistribuídas ou documentação corporativa de terceiros, leia integralmente o arquivo LICENSE na raiz do repositório para cumprir as quatro cláusulas da licença BSD.

## Exemplo
Em uma auditoria de licenças de ferramentas de verificação (comparando, por exemplo, Kani sob MIT/Apache-2.0 e CBMC como backend), o registro correto para o CBMC conforme seu README é 4-clause BSD.

## Limites e trade-offs
Esta nota registra apenas a declaração oficial da seção License do README; a interpretação jurídica das cláusulas para redistribuição comercial cabe à leitura direta do arquivo LICENSE do projeto.

## Como verificar
Conferi a seção License no final do README oficial do repositório diffblue/cbmc.

## Conexões
- [[cbmc-compilers-and-build-from-source]] — Veja também: Compilação a partir do código-fonte via COMPILING.md e qualidade monitorada.

## Fontes
- [CBMC — README oficial](https://raw.githubusercontent.com/diffblue/cbmc/develop/README.md) — README oficial do CBMC com suporte a C89–C23, extensões gcc/Visual Studio, SystemC/Scoot, Verilog, loop unwinding, canais release vs develop, instalação em Windows/Linux/macOS, contribuição e licença 4-clause BSD.; consultado em 2026-10-03.
- [Repositório oficial diffblue/cbmc](https://github.com/diffblue/cbmc) — Repositório oficial do CBMC e da suíte CProver no GitHub com releases, TOOLS_OVERVIEW.md, COMPILING.md, CODING_STANDARD.md e FEATURE_IDEAS.md.; consultado em 2026-10-03.
