---
id: software.seguranca.tranche19.001804
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

# SPIFFE/SPIRE: Atestação de nó antes da emissão

## Em uma frase
**SPIFFE/SPIRE — Atestação de nó antes da emissão:** Node attestation prova atributos do host ao agent ou servidor antes de aceitar sua participação.

## Por que importa
O recorte de **atestação de nó antes da emissão** ajuda a substituir credenciais estáticas por identidade de workload verificável, com emissão e rotação automatizadas. A equipe registra risco, evidência e responsável.

## Como funciona
Para **atestação de nó antes da emissão**, SPIRE atesta nós e workloads e emite SVIDs associados ao trust domain; consumidores validam identidade e trust bundle. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Configure um attestor compatível com o ambiente e recuse nó de teste sem atributo esperado. Teste em staging autorizado.

## Limites e trade-offs
Atestação baseada em valor reutilizável pode ser clonada se o bootstrap não for protegido. Exceções exigem responsável e prazo.

## Como verificar
Teste um host válido e outro sem prova e confirme que somente o esperado recebe identidade de agent. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[spiffe-spire-atestar-workload-por-seletores]] — Complementa o tópico com spiffe/spire: atestar workload por seletores.

## Fontes
- [SPIRE — Concepts](https://spiffe.io/docs/latest/spire-about/spire-concepts/) — documentação oficial de trust domains, agents, attestation, SVIDs e bundles; consultado em 2026-10-04.
- [SPIRE — Configuration](https://spiffe.io/docs/latest/deploying/configuring/) — guia oficial de configuração de servidores, agents, attestors e workload registration; consultado em 2026-10-04.
