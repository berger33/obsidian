---
id: software.seguranca.tranche19.001819
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

# HashiCorp Vault: Rotacionar service account sem indisponibilidade

## Em uma frase
**HashiCorp Vault — Rotacionar service account sem indisponibilidade:** Mudanças em tokens, audiences e roles Kubernetes devem ser coordenadas com workloads consumidores.

## Por que importa
O recorte de **rotacionar service account sem indisponibilidade** ajuda a centralizar acesso a segredos e reduzir credenciais estáticas em workloads e serviços. A equipe registra risco, evidência e responsável.

## Como funciona
Para **rotacionar service account sem indisponibilidade**, um cliente autentica em método habilitado, recebe token limitado por policy e acessa caminhos ou leases autorizados. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Faça rotação em namespace de staging com réplica canary e valide novo login antes de remover configuração antiga. Teste em staging autorizado.

## Limites e trade-offs
Remover role ou audience cedo demais pode impedir reconexão de pods já iniciados. Exceções exigem responsável e prazo.

## Como verificar
Teste rollout progressivo, reconexão e revogação de token antigo em janela controlada. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[vault-auditar-cliente-e-ciclo-de-credencial]] — Complementa o tópico com hashicorp vault: auditar cliente e ciclo de credencial.

## Fontes
- [HashiCorp Vault — Lease concepts](https://developer.hashicorp.com/vault/docs/concepts/lease) — documentação oficial de TTL, renovação e revogação de leases; consultado em 2026-10-04.
- [HashiCorp Vault — Kubernetes auth method](https://developer.hashicorp.com/vault/docs/auth/kubernetes) — guia oficial de autenticação Kubernetes, roles e service account tokens; consultado em 2026-10-04.
