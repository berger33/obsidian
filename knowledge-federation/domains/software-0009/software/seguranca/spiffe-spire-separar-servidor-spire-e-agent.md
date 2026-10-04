---
id: software.seguranca.tranche19.001803
tipo: tecnica
dominio: software
subdominio: seguranca
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-04
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-04
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-19.md"
fontes: ["https://spiffe.io/docs/latest/spire-about/spire-concepts/", "https://spiffe.io/docs/latest/deploying/configuring/"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# SPIFFE/SPIRE: Separar servidor SPIRE e agent

## Em uma frase
**SPIFFE/SPIRE — Separar servidor SPIRE e agent:** O servidor administra registration entries e bundles; agents atestam o nó e servem workloads locais.

## Por que importa
O recorte de **separar servidor spire e agent** ajuda a substituir credenciais estáticas por identidade de workload verificável, com emissão e rotação automatizadas. A equipe registra risco, evidência e responsável.

## Como funciona
Para **separar servidor spire e agent**, SPIRE atesta nós e workloads e emite SVIDs associados ao trust domain; consumidores validam identidade e trust bundle. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Implante um agent por nó de teste e registre comunicação controlada com o servidor SPIRE. Teste em staging autorizado.

## Limites e trade-offs
Comprometer um agent ou servidor pode alterar identidades ou credenciais dentro do seu alcance. Exceções exigem responsável e prazo.

## Como verificar
Verifique mTLS, autorização, versão e health de ambas as funções em uma instalação de laboratório. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[spiffe-spire-atestacao-de-no-antes-da-emissao]] — Complementa o tópico com spiffe/spire: atestação de nó antes da emissão.

## Fontes
- [SPIRE — Concepts](https://spiffe.io/docs/latest/spire-about/spire-concepts/) — documentação oficial de trust domains, agents, attestation, SVIDs e bundles; consultado em 2026-10-04.
- [SPIRE — Configuration](https://spiffe.io/docs/latest/deploying/configuring/) — guia oficial de configuração de servidores, agents, attestors e workload registration; consultado em 2026-10-04.
