---
id: software.seguranca.tranche19.001814
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

# HashiCorp Vault: Autenticar workload Kubernetes

## Em uma frase
**HashiCorp Vault — Autenticar workload Kubernetes:** Método Kubernetes permite que workloads usem token de service account para obter token Vault associado a role.

## Por que importa
O recorte de **autenticar workload kubernetes** ajuda a centralizar acesso a segredos e reduzir credenciais estáticas em workloads e serviços. A equipe registra risco, evidência e responsável.

## Como funciona
Para **autenticar workload kubernetes**, um cliente autentica em método habilitado, recebe token limitado por policy e acessa caminhos ou leases autorizados. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Crie role de teste vinculada a service account e namespace específicos antes de habilitar aplicação. Teste em staging autorizado.

## Limites e trade-offs
Trust de JWT e configuração do TokenReview precisam permanecer consistentes com o cluster. Exceções exigem responsável e prazo.

## Como verificar
Autentique service account autorizada e confirme rejeição de token de namespace diferente. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[vault-limitar-role-a-service-account-e-namespace]] — Complementa o tópico com hashicorp vault: limitar role a service account e namespace.

## Fontes
- [HashiCorp Vault — Lease concepts](https://developer.hashicorp.com/vault/docs/concepts/lease) — documentação oficial de TTL, renovação e revogação de leases; consultado em 2026-10-04.
- [HashiCorp Vault — Kubernetes auth method](https://developer.hashicorp.com/vault/docs/auth/kubernetes) — guia oficial de autenticação Kubernetes, roles e service account tokens; consultado em 2026-10-04.
