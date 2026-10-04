---
id: software.devops.tranche20.001944
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

# OpenBao KV Secrets Engine v2 (`kv-v2`): versionamento de segredos, *Check-and-Set (CAS)* e recuperação de deleções

## Em uma frase
O motor de segredos estáticos **`kv-v2`** do OpenBao (`bao secrets enable -version=2 kv`) armazena pares chave/valor arbitrários mantendo um histórico configurável de versões (`max_versions`, padrão 10), suportando operações de **Check-and-Set (`-cas`)**, *soft delete* (`bao kv delete`), restauração (`bao kv undelete`) e destruição permanente (`bao kv destroy`).

## Por que importa
Em um store chave-valor simples sem versionamento nem trava otimista, se dois pipelines atualizarem o mesmo caminho simultaneamente, o último sobrescreve o anterior silenciosamente e não há como reverter rapidamente para a versão anterior.

## Como funciona
Com o parâmetro `-cas=<versao_atual>` (ou `cas_required=true` na configuração do segredo/engine), o OpenBao só aceita a escrita se a versão atual no servidor coincidir exatamente com o número informado; por exemplo, `-cas=0` garante que o segredo só será gravado se ainda não existir.

## Exemplo
```bash
bao secrets enable -path=secret kv-v2
bao kv put -mount=secret prod/payment-api api_key="live_abc123" timeout="30s"
bao kv put -mount=secret -cas=1 prod/payment-api api_key="live_ rotated456" timeout="30s"
bao kv get -mount=secret -version=1 prod/payment-api
```

## Limites e trade-offs
Lembre-se de que `bao kv delete` realiza apenas uma exclusão lógica (*soft delete* — marcando a versão como deletada, mas reversível com `undelete`); para apagar criptograficamente uma versão vazada de forma irreversível, use `bao kv destroy -versions=1`.

## Como verificar
Execute `bao kv metadata get -mount=secret prod/payment-api` para auditar todas as versões existentes, timestamps e estado de deleção/destruição.

## Conexões
- [[openbao-seal-unseal-shamir-auto-unseal-kms-pkcs11-inicializacao]] — Veja também: OpenBao Seal/Unseal e Inicialização: chaves Shamir vs Auto-Unseal com KMS/PKCS#11 e inicialização declarativa.
- [[openbao-dynamic-secrets-leases-renewal-revocation-database-k8s]] — Veja também: OpenBao Dynamic Secrets, Leases e Revogação: credenciais sob demanda para bancos SQL, AWS e Kubernetes com TTL automático.

## Fontes
- [OpenBao GitHub — README.md (OpenSSF/Linux Foundation Community-Driven Secrets & Encryption Management System)](https://raw.githubusercontent.com/openbao/openbao/main/README.md) — README oficial do openbao/openbao apresentando governança OpenSSF sob MPL-2.0, compilação e documentação; consultado em 2026-10-03.
- [OpenBao Official Documentation — What is OpenBao? (Authenticate/Validate/Authorize/Access Pipeline, Dynamic Secrets, Leasing & Revocation)](https://openbao.org/docs/what-is-openbao/) — Documentação oficial de arquitetura do OpenBao explicando o fluxo de 4 estágios (Authenticate, Validate, Authorize, Access), segredos dinâmicos, leases e revogação; consultado em 2026-10-03.
- [OpenBao — Official GitHub Repository](https://github.com/openbao/openbao) — Repositório oficial MPL-2.0 do OpenBao na OpenSSF; consultado em 2026-10-03.
