---
id: software.testes.tranche23.001711
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-23.md"
fontes: ["https://github.com/AFLplusplus/AFLplusplus/blob/stable/README.md", "https://hub.docker.com/r/aflplusplus/aflplusplus"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Licença AGPL com harness Apache, Docker pronto e branches stable/dev

## Em uma frase
O README oficial documenta uma estrutura de licença dupla deliberada: o AFL++ é AGPL-3.0-or-later e contém arquivos Apache-2.0, mas "Everything compiled into a fuzzing harness is and will stay Apache 2.0 licensed", cada arquivo declara sua licença em cabeçalho SPDX — e uma licença comercial opcional existe para quem não pode usar AGPL, obtida por doação ("the project and its maintainers receive no money").

## Por que importa
A cláusula do harness responde a objeção jurídica clássica de fuzzing corporativo: instrumentar seu produto não puxa o alvo para a AGPL, só as ferramentas em torno dele — isso está escrito na página oficial, não em interpretação.

## Como funciona
A distribuição recomendada no README tem dois caminhos: puxar a imagem Docker aflplusplus/aflplusplus (atualizada a cada push na stable; x86_64 e arm64), com o alvo montado em /src, ou compilar você mesmo seguindo docs/INSTALL.md — "which we recommend".

## Exemplo
Antes de adotar, abra o LICENSING.md referenciado pelo README e confirme o enquadramento plain-language; em paralelo, valide seu pipeline compilando da fonte estável para ver o inventário real de ferramentas geradas.

## Limites e trade-offs
O texto sobre a licença comercial menciona doação a "uma boa causa" sem contrato de SLA; quem precisa de suporte comercial formal não encontra isso na licença documentada, e o README mesmo dirence para o LICENSING.md em vez de resumir exceções.

## Como verificar
Confirme na seção License e Getting Started do README stable o triplo AGPL/Apache-2.0/SPDX, o parágrafo da licença comercial, os comandos docker pull e a política de branches (PRs só no dev; stable é a default).

## Conexões
- [[aflpp-what-it-is]] — Veja também: AFL++: o fork superior ao AFL do Google, na série 5.03c.
- [[aflpp-compiler-modes]] — Veja também: afl-cc: a árvore de decisão LTO, LLVM e GCC_PLUGIN.

## Fontes
- [AFL++ — README oficial (stable)](https://github.com/AFLplusplus/AFLplusplus/blob/stable/README.md) — versão 5.03c, licenças, quick start, Docker e branches; consultado em 2026-10-03.
- [AFL++ — imagem no Docker Hub](https://hub.docker.com/r/aflplusplus/aflplusplus) — registry da imagem que o README oficial manda puxar; consultado em 2026-10-03.
