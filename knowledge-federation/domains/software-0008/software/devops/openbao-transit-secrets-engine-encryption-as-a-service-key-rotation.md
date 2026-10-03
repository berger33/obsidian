---
id: software.devops.tranche20.001946
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

# OpenBao Transit Secrets Engine (*Encryption as a Service*): criptografia em trânsito sem armazenar dados, assinaturas e rotação de chaves

## Em uma frase
O **Transit Secrets Engine** (`bao secrets enable transit`) oferece *Encryption as a Service*: ele criptografa (`transit/encrypt/<key>`), descriptografa (`transit/decrypt/<key>`), assina dados e gera HMACs sem armazenar o payload no OpenBao, permitindo que os desenvolvedores gravem o texto cifrado (`vault:v1:...`) em qualquer banco SQL ou bucket S3.

## Por que importa
Implementar criptografia AES-GCM ou gerenciamento de nonces e rotação de chaves diretamente no código de cada microsserviço frequentemente leva a erros criptográficos graves.

## Como funciona
Quando a equipe de segurança rotaciona uma chave no Transit com `bao write -f transit/keys/customer-pii/rotate`, a chave passa para a versão `v2`: novos dados são cifrados com `v2` (`vault:v2:...`), dados antigos `vault:v1:...` continuam sendo decifrados normalmente e o endpoint `transit/rewrap/customer-pii` re-criptografa registros antigos para `v2` sem nunca expor o texto em claro à aplicação.

## Exemplo
```bash
bao secrets enable transit
bao write -f transit/keys/customer-pii
bao write transit/encrypt/customer-pii plaintext=$(echo -n "cpf-12345678900" | base64)
bao write -f transit/keys/customer-pii/rotate
```

## Limites e trade-offs
Definir `min_decryption_version` em uma chave Transit após concluir o `rewrap` do banco de dados invalida permanentemente qualquer texto cifrado antigo que tenha sido assinado com versões legadas da chave.

## Como verificar
Execute `bao read transit/keys/customer-pii` para verificar a versão mais recente (`latest_version`) e a versão mínima de decriptação da chave.

## Conexões
- [[openbao-dynamic-secrets-leases-renewal-revocation-database-k8s]] — Veja também: OpenBao Dynamic Secrets, Leases e Revogação: credenciais sob demanda para bancos SQL, AWS e Kubernetes com TTL automático.
- [[openbao-politicas-hcl-path-capabilities-least-privilege-tokens]] — Veja também: OpenBao Políticas HCL (*Path-Based Policies*): controle declarativo de capacidades (`create`, `read`, `update`, `delete`, `list`, `sudo`).

## Fontes
- [OpenBao GitHub — README.md (OpenSSF/Linux Foundation Community-Driven Secrets & Encryption Management System)](https://raw.githubusercontent.com/openbao/openbao/main/README.md) — README oficial do openbao/openbao apresentando governança OpenSSF sob MPL-2.0, compilação e documentação; consultado em 2026-10-03.
- [OpenBao Official Documentation — What is OpenBao? (Authenticate/Validate/Authorize/Access Pipeline, Dynamic Secrets, Leasing & Revocation)](https://openbao.org/docs/what-is-openbao/) — Documentação oficial de arquitetura do OpenBao explicando o fluxo de 4 estágios (Authenticate, Validate, Authorize, Access), segredos dinâmicos, leases e revogação; consultado em 2026-10-03.
- [OpenBao — Official GitHub Repository](https://github.com/openbao/openbao) — Repositório oficial MPL-2.0 do OpenBao na OpenSSF; consultado em 2026-10-03.
