---
id: software.seguranca.tranche19.001808
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

# SPIFFE/SPIRE: Distribuir trust bundles com rotação

## Em uma frase
**SPIFFE/SPIRE — Distribuir trust bundles com rotação:** Trust bundle contém material para validar identidades e deve ser atualizado sem interromper confiança entre peers.

## Por que importa
O recorte de **distribuir trust bundles com rotação** ajuda a substituir credenciais estáticas por identidade de workload verificável, com emissão e rotação automatizadas. A equipe registra risco, evidência e responsável.

## Como funciona
Para **distribuir trust bundles com rotação**, SPIRE atesta nós e workloads e emite SVIDs associados ao trust domain; consumidores validam identidade e trust bundle. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Planeje sobreposição de certificados antigos e novos em teste antes de rotacionar autoridade. Teste em staging autorizado.

## Limites e trade-offs
Bundle desatualizado pode interromper conexões; confiança excessiva pode aceitar emissor indevido. Exceções exigem responsável e prazo.

## Como verificar
Teste verificação durante e após rotação e confirme remoção do material antigo no prazo definido. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[spiffe-spire-federar-trust-domains]] — Complementa o tópico com spiffe/spire: federar trust domains.

## Fontes
- [SPIRE — Concepts](https://spiffe.io/docs/latest/spire-about/spire-concepts/) — documentação oficial de trust domains, agents, attestation, SVIDs e bundles; consultado em 2026-10-04.
- [SPIRE — Configuration](https://spiffe.io/docs/latest/deploying/configuring/) — guia oficial de configuração de servidores, agents, attestors e workload registration; consultado em 2026-10-04.
