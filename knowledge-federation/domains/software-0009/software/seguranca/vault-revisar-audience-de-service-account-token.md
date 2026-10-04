---
id: software.seguranca.tranche19.001816
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
fontes: ["https://developer.hashicorp.com/vault/docs/concepts/lease", "https://developer.hashicorp.com/vault/docs/auth/kubernetes"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# HashiCorp Vault: Revisar audience de service account token

## Em uma frase
**HashiCorp Vault — Revisar audience de service account token:** Audience vincula o token de service account ao destinatário esperado quando configurado para autenticação.

## Por que importa
O recorte de **revisar audience de service account token** ajuda a centralizar acesso a segredos e reduzir credenciais estáticas em workloads e serviços. A equipe registra risco, evidência e responsável.

## Como funciona
Para **revisar audience de service account token**, um cliente autentica em método habilitado, recebe token limitado por policy e acessa caminhos ou leases autorizados. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Defina audience compatível na role e no token projetado de workload de teste. Teste em staging autorizado.

## Limites e trade-offs
Audience ausente ou incompatível pode causar recusa ou aceitar token destinado a outro serviço. Exceções exigem responsável e prazo.

## Como verificar
Inspecione claims sem expor token e teste validação com audience correta e incorreta. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[vault-aplicar-policy-de-menor-privilegio]] — Complementa o tópico com hashicorp vault: aplicar policy de menor privilégio.

## Fontes
- [HashiCorp Vault — Lease concepts](https://developer.hashicorp.com/vault/docs/concepts/lease) — documentação oficial de TTL, renovação e revogação de leases; consultado em 2026-10-04.
- [HashiCorp Vault — Kubernetes auth method](https://developer.hashicorp.com/vault/docs/auth/kubernetes) — guia oficial de autenticação Kubernetes, roles e service account tokens; consultado em 2026-10-04.
