---
id: software.devops.tranche20.001943
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
fontes: ["https://openbao.org/docs/what-is-openbao/", "https://raw.githubusercontent.com/openbao/openbao/main/README.md", "https://github.com/openbao/openbao"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# OpenBao Seal/Unseal e Inicialização: chaves Shamir vs Auto-Unseal com KMS/PKCS#11 e inicialização declarativa

## Em uma frase
Todo servidor OpenBao inicia em estado **lacrado (`Sealed: true`)**, no qual ele conhece a localização do armazenamento cifrado mas não possui em memória a chave mestra necessária para decifrar a chave de criptografia da barreira, podendo ser deslacrado manualmente via **Shamir's Secret Sharing** (`bao operator unseal`) ou automaticamente via **Auto-Unseal** (Cloud KMS, Transit de outro OpenBao ou HSM PKCS#11).

## Por que importa
Em um cluster Kubernetes onde Pods do OpenBao podem ser reagendados em outros nós durante upgrades de kernel, exigir que 3 operadores humanos digitem partes de chave Shamir manualmente a cada restart deixaria osPods indisponíveis.

## Como funciona
Com um bloco `seal "awskms"`, `seal "gcpckms"`, `seal "transit"` ou `seal "pkcs11"` no `config.hcl`, o OpenBao cifra sua chave raiz usando o KMS/HSM externo e deslacra-se automaticamente ao iniciar (`Recovery Keys` substituem as chaves de unseal manuais).

## Exemplo
```bash
# Inicializando um cluster OpenBao com 5 fragmentos de chave e quórum de 3:
bao operator init -key-shares=5 -key-threshold=3
bao operator unseal
```

## Limites e trade-offs
Distribua os fragmentos de chave (`Unseal Keys` ou `Recovery Keys`) entre custodiantes distintos e nunca os armazene juntos no mesmo cofre ou repositório.

## Como verificar
Execute `bao status` após o boot do Pod para confirmar `Initialized: true` e `Sealed: false`.

## Conexões
- [[openbao-storage-backends-raft-integrado-postgresql-ha-clustering]] — Veja também: OpenBao Storage Backends e Alta Disponibilidade: armazenamento integrado `raft` vs `postgresql` e barreira criptográfica.
- [[openbao-secrets-engines-kv-v2-versionamento-cas-soft-delete]] — Veja também: OpenBao KV Secrets Engine v2 (`kv-v2`): versionamento de segredos, *Check-and-Set (CAS)* e recuperação de deleções.

## Fontes
- [OpenBao GitHub — README.md (OpenSSF/Linux Foundation Community-Driven Secrets & Encryption Management System)](https://openbao.org/docs/what-is-openbao/) — README oficial do openbao/openbao apresentando governança OpenSSF sob MPL-2.0, compilação e documentação; consultado em 2026-10-03.
- [OpenBao Official Documentation — What is OpenBao? (Authenticate/Validate/Authorize/Access Pipeline, Dynamic Secrets, Leasing & Revocation)](https://raw.githubusercontent.com/openbao/openbao/main/README.md) — Documentação oficial de arquitetura do OpenBao explicando o fluxo de 4 estágios (Authenticate, Validate, Authorize, Access), segredos dinâmicos, leases e revogação; consultado em 2026-10-03.
- [OpenBao — Official GitHub Repository](https://github.com/openbao/openbao) — Repositório oficial MPL-2.0 do OpenBao na OpenSSF; consultado em 2026-10-03.
