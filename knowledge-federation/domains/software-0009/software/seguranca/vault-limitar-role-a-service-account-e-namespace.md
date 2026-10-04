---
id: software.seguranca.tranche19.001815
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

# HashiCorp Vault: Limitar role a service account e namespace

## Em uma frase
**HashiCorp Vault — Limitar role a service account e namespace:** A role Kubernetes pode restringir quais service accounts e namespaces podem autenticar e quais policies recebem.

## Por que importa
O recorte de **limitar role a service account e namespace** ajuda a centralizar acesso a segredos e reduzir credenciais estáticas em workloads e serviços. A equipe registra risco, evidência e responsável.

## Como funciona
Para **limitar role a service account e namespace**, um cliente autentica em método habilitado, recebe token limitado por policy e acessa caminhos ou leases autorizados. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Vincule role de leitura a `app-reader` no namespace de staging e atribua policy mínima. Teste em staging autorizado.

## Limites e trade-offs
Wildcard em service account ou namespace amplia acesso a pods futuros. Exceções exigem responsável e prazo.

## Como verificar
Tente autenticar conta nomeada e uma conta não listada e compare policies do token. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[vault-revisar-audience-de-service-account-token]] — Complementa o tópico com hashicorp vault: revisar audience de service account token.

## Fontes
- [HashiCorp Vault — Lease concepts](https://developer.hashicorp.com/vault/docs/concepts/lease) — documentação oficial de TTL, renovação e revogação de leases; consultado em 2026-10-04.
- [HashiCorp Vault — Kubernetes auth method](https://developer.hashicorp.com/vault/docs/auth/kubernetes) — guia oficial de autenticação Kubernetes, roles e service account tokens; consultado em 2026-10-04.
