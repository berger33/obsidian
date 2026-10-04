---
id: software.devops.tranche20.001941
tipo: tecnica
dominio: software
subdominio: devops
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-20.md"
fontes: ["https://raw.githubusercontent.com/openbao/openbao/main/README.md", "https://openbao.org/docs/what-is-openbao/", "https://github.com/openbao/openbao"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# OpenBao: arquitetura do sistema open-source (OpenSSF/Linux Foundation) de gerenciamento de segredos e criptografia (`bao`)

## Em uma frase
O **OpenBao** (projeto sob governança aberta da Linux Foundation / OpenSSF licenciado sob MPL 2.0, originado como fork comunitário do HashiCorp Vault) é uma plataforma baseada em identidade para armazenar, gerar dinamicamente e distribuir dados sensíveis — incluindo segredos, certificados X.509 e chaves criptográficas — acessada via CLI **`bao`**, API HTTP ou Web UI.

## Por que importa
A mudança de licença do Vault tradicional para BSL motivou a comunidade cloud-native a manter no OpenBao uma solução 100% open-source OSI-approved compatível com a API/CLI, adicionando recursos comunitários como suporte a armazenamento **PostgreSQL** transacional, escalabilidade horizontal e namespaces abertos.

## Como funciona
Conforme a documentação oficial (`what-is-openbao`), todo acesso no OpenBao percorre quatro estágios: 1) **Authenticate** (o cliente apresenta credenciais via Kubernetes Auth, OIDC, JWT, AppRole, GitHub ou LDAP); 2) **Validate** (o OpenBao valida na fonte confiável e emite um token); 3) **Authorize** (o token é avaliado contra políticas declarativas baseadas em caminho *path-based*); e 4) **Access** (o cliente lê segredos, gera credenciais dinâmicas com *lease* ou executa criptografia Transit).

## Exemplo
```bash
# Iniciando o servidor OpenBao em modo de desenvolvimento local e verificando seu status:
bao server -dev
export BAO_ADDR='http://127.0.0.1:8200'
bao status
```

## Limites e trade-offs
O modo `bao server -dev` executa inteiramente em memória já deslacrado (*unsealed*) e imprime o token root no terminal apenas para desenvolvimento e testes locais — jamais utilize `-dev` em produção.

## Como verificar
Execute `bao status` para inspecionar o estado `Initialized`, `Sealed`, versão do servidor e tipo de storage ativo.

## Conexões
- [[openbao-storage-backends-raft-integrado-postgresql-ha-clustering]] — Veja também: OpenBao Storage Backends e Alta Disponibilidade: armazenamento integrado `raft` vs `postgresql` e barreira criptográfica.

## Fontes
- [OpenBao GitHub — README.md (OpenSSF/Linux Foundation Community-Driven Secrets & Encryption Management System)](https://raw.githubusercontent.com/openbao/openbao/main/README.md) — README oficial do openbao/openbao apresentando governança OpenSSF sob MPL-2.0, compilação e documentação; consultado em 2026-10-03.
- [OpenBao Official Documentation — What is OpenBao? (Authenticate/Validate/Authorize/Access Pipeline, Dynamic Secrets, Leasing & Revocation)](https://openbao.org/docs/what-is-openbao/) — Documentação oficial de arquitetura do OpenBao explicando o fluxo de 4 estágios (Authenticate, Validate, Authorize, Access), segredos dinâmicos, leases e revogação; consultado em 2026-10-03.
- [OpenBao — Official GitHub Repository](https://github.com/openbao/openbao) — Repositório oficial MPL-2.0 do OpenBao na OpenSSF; consultado em 2026-10-03.
