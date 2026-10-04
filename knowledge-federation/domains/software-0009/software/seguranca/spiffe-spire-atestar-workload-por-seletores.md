---
id: software.seguranca.tranche19.001805
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

# SPIFFE/SPIRE: Atestar workload por seletores

## Em uma frase
**SPIFFE/SPIRE — Atestar workload por seletores:** Workload attestation relaciona o processo a atributos observáveis e os compara a seletores de uma registration entry.

## Por que importa
O recorte de **atestar workload por seletores** ajuda a substituir credenciais estáticas por identidade de workload verificável, com emissão e rotação automatizadas. A equipe registra risco, evidência e responsável.

## Como funciona
Para **atestar workload por seletores**, SPIRE atesta nós e workloads e emite SVIDs associados ao trust domain; consumidores validam identidade e trust bundle. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Registre serviço de laboratório por namespace e service account em vez de conceder SVID a qualquer processo do nó. Teste em staging autorizado.

## Limites e trade-offs
Seletor baseado em atributo mutável ou muito amplo pode conceder identidade a workload imprevisto. Exceções exigem responsável e prazo.

## Como verificar
Crie workload que difere em um atributo e confirme que ele não corresponde ao registro. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[spiffe-spire-restringir-registration-entries]] — Complementa o tópico com spiffe/spire: restringir registration entries.

## Fontes
- [SPIRE — Concepts](https://spiffe.io/docs/latest/spire-about/spire-concepts/) — documentação oficial de trust domains, agents, attestation, SVIDs e bundles; consultado em 2026-10-04.
- [SPIRE — Configuration](https://spiffe.io/docs/latest/deploying/configuring/) — guia oficial de configuração de servidores, agents, attestors e workload registration; consultado em 2026-10-04.
