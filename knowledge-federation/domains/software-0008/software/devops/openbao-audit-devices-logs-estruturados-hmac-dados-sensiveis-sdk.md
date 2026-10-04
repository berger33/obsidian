---
id: software.devops.tranche20.001950
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

# OpenBao Audit Devices e SDK Go (`api/v2`): trilha de auditoria à prova de falha com HMAC e bibliotecas oficiais

## Em uma frase
O OpenBao garante rastreabilidade completa de todas as requisições e respostas que passam pelo servidor por meio dos **Audit Devices** (`file`, `syslog`, `socket`), onde todos os valores sensíveis nos logs de auditoria são automaticamente mascarados com **HMAC-SHA256**, e disponibiliza os pacotes Go oficiais `github.com/openbao/openbao/api/v2` e `sdk/v2`.

## Por que importa
Se um invasor obtiver um token válido e ler segredos, sem um log de auditoria imutável você jamais saberá quais caminhos foram acessados; por outro lado, se o log de auditoria falhar (ex.: disco cheio), permitir que segredos continuem sendo lidos sem registro violaria o compliance.

## Como funciona
Por design de segurança *fail-closed*, assim que pelo menos um Audit Device é habilitado (`bao audit enable file file_path=/var/log/openbao/audit.log`), o OpenBao **recusa processar qualquer requisição** caso não consiga gravar o evento em pelo menos um Audit Device ativo. Por isso, em produção recomenda-se habilitar dois Audit Devices independentes (ex.: `file` + `syslog`).

## Exemplo
```bash
# Habilitando auditoria estruturada em arquivo e listando os dispositivos ativos:
bao audit enable file file_path=/var/log/openbao/audit.log
bao audit list -detailed
```

## Limites e trade-offs
Conforme destacado no README oficial do repositório `openbao/openbao`, projetos em Go que integram com o OpenBao devem importar exclusivamente `github.com/openbao/openbao/api/v2` (ou `sdk/v2`), e nunca o módulo interno da aplicação principal.

## Como verificar
Execute `bao audit list` e verifique no arquivo JSON de auditoria que os tokens e segredos aparecem protegidos por prefixo `hmac-sha256:...`.

## Conexões
- [[openbao-pki-secrets-engine-ca-interna-acme-emissao-certificados]] — Veja também: OpenBao PKI Secrets Engine: operação de CA Intermediária X.509 interna, suporte a ACME e emissão de certificados TLS efêmeros.

## Fontes
- [OpenBao GitHub — README.md (OpenSSF/Linux Foundation Community-Driven Secrets & Encryption Management System)](https://raw.githubusercontent.com/openbao/openbao/main/README.md) — README oficial do openbao/openbao apresentando governança OpenSSF sob MPL-2.0, compilação e documentação; consultado em 2026-10-03.
- [OpenBao Official Documentation — What is OpenBao? (Authenticate/Validate/Authorize/Access Pipeline, Dynamic Secrets, Leasing & Revocation)](https://openbao.org/docs/what-is-openbao/) — Documentação oficial de arquitetura do OpenBao explicando o fluxo de 4 estágios (Authenticate, Validate, Authorize, Access), segredos dinâmicos, leases e revogação; consultado em 2026-10-03.
- [OpenBao — Official GitHub Repository](https://github.com/openbao/openbao) — Repositório oficial MPL-2.0 do OpenBao na OpenSSF; consultado em 2026-10-03.
