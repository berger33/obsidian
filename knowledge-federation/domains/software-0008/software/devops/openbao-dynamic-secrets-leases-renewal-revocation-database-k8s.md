---
id: software.devops.tranche20.001945
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

# OpenBao Dynamic Secrets, Leases e Revogação: credenciais sob demanda para bancos SQL, AWS e Kubernetes com TTL automático

## Em uma frase
Os motores de **Dynamic Secrets** do OpenBao (como `database`, `aws` e `kubernetes`) geram credenciais exclusivas sob demanda no exato momento em que uma aplicação as solicita, anexando a cada credencial um **`lease_id`** com tempo de vida (`ttl` e `max_ttl`) que é revogado automaticamente pelo OpenBao ao expirar.

## Por que importa
Quando 20 réplicas de um microsserviço compartilham o mesmo usuário e senha estáticos do PostgreSQL, é impossível saber nos logs do banco qual réplica executou uma query suspeita, e rotacionar a senha derruba as réplicas que não recarregarem a tempo.

## Como funciona
Com o motor `database` configurado no OpenBao, cada Pod lê `database/creds/readonly-role` e recebe um par `username`/`password` recém-criado no PostgreSQL exclusivamente para aquele Pod. O cliente renova o lease periodicamente via `bao lease renew` e, quando o Pod encerra ou o lease expira, o OpenBao executa `DROP ROLE` automaticamente no banco.

## Exemplo
```bash
# Lendo uma credencial dinâmica, renovando seu lease e testando a revogação em árvore:
bao read database/creds/app-readonly
bao lease renew database/creds/app-readonly/2f6a9c...
bao lease revoke -prefix database/creds/app-readonly
```

## Limites e trade-offs
Conforme destacado na documentação oficial do OpenBao, `bao lease revoke -prefix <caminho>` permite revogar instantaneamente toda uma **árvore** de segredos dinâmicos de uma só vez durante a resposta a uma intrusão.

## Como verificar
Gere uma credencial dinâmica com `bao read`, verifique o `lease_duration` e confirme sua remoção no sistema alvo após `bao lease revoke`.

## Conexões
- [[openbao-secrets-engines-kv-v2-versionamento-cas-soft-delete]] — Veja também: OpenBao KV Secrets Engine v2 (`kv-v2`): versionamento de segredos, *Check-and-Set (CAS)* e recuperação de deleções.
- [[openbao-transit-secrets-engine-encryption-as-a-service-key-rotation]] — Veja também: OpenBao Transit Secrets Engine (*Encryption as a Service*): criptografia em trânsito sem armazenar dados, assinaturas e rotação de chaves.

## Fontes
- [OpenBao GitHub — README.md (OpenSSF/Linux Foundation Community-Driven Secrets & Encryption Management System)](https://raw.githubusercontent.com/openbao/openbao/main/README.md) — README oficial do openbao/openbao apresentando governança OpenSSF sob MPL-2.0, compilação e documentação; consultado em 2026-10-03.
- [OpenBao Official Documentation — What is OpenBao? (Authenticate/Validate/Authorize/Access Pipeline, Dynamic Secrets, Leasing & Revocation)](https://openbao.org/docs/what-is-openbao/) — Documentação oficial de arquitetura do OpenBao explicando o fluxo de 4 estágios (Authenticate, Validate, Authorize, Access), segredos dinâmicos, leases e revogação; consultado em 2026-10-03.
- [OpenBao — Official GitHub Repository](https://github.com/openbao/openbao) — Repositório oficial MPL-2.0 do OpenBao na OpenSSF; consultado em 2026-10-03.
