---
id: software.seguranca.tranche03.000239
tipo: tecnica
dominio: software
subdominio: seguranca
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-03.md"
fontes: ["https://raw.githubusercontent.com/dexidp/dex/master/README.md", "https://dexidp.io/docs/connectors/", "https://github.com/dexidp/dex"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Dex API Administrativa `gRPC` com `mTLS`: criação dinâmica de clientes OAuth2 e revogação de Refresh Tokens

## Em uma frase
Além do servidor HTTP/HTTPS OIDC (porta `5556`), o Dex pode expor uma **API gRPC administrativa** (tipicamente na porta `5557`) protegida por **mTLS (`clientCA`)** para criar, atualizar e deletar clientes OAuth2 dinamicamente, gerenciar senhas (se o conector local estiver ativo) e listar/revogar `refresh_tokens` de usuários sem reiniciar o servidor.

## Por que importa
Em plataformas multi-tenant onde novos serviços ou clusters são provisionados automaticamente por operadores Kubernetes, reiniciar o Dex a cada novo cliente adicionado em `staticClients` é inviável.

## Como funciona
Configurando `grpc.tlsCert`, `grpc.tlsKey` e **`grpc.tlsClientCA`** no `config.yaml`, o Dex exige autenticação mútua por certificado X.509 de cliente em toda chamada gRPC, garantindo que apenas o controlador autorizado possa registrar novos clientes OAuth2.

## Exemplo
```yaml
grpc:
  addr: 0.0.0.0:5557
  tlsCert: /etc/dex/grpc-tls/server.crt
  tlsKey: /etc/dex/grpc-tls/server.key
  tlsClientCA: /etc/dex/grpc-tls/client-ca.crt
  reflection: false
```

## Limites e trade-offs
Nunca exponha a porta gRPC (`5557`) sem `tlsClientCA` configurado nem através do Ingress público: ela é uma API administrativa de controle interno do cluster.

## Como verificar
Verifique que conexões à porta `5557` sem um certificado assinado pela `tlsClientCA` são rejeitadas durante o handshake TLS.

## Conexões
- [[dexidp-storage-backends-kubernetes-crd-postgres-sqlite-etcd]] — Veja também: Dex Backends de Armazenamento (`storage`): `kubernetes` (CRDs nativos) vs `postgres` / `mysql` / `etcd` em Alta Disponibilidade.
- [[dexidp-token-exchange-rfc8693-aws-sts-irsa-workload-identity]] — Veja também: Dex como Emissor OIDC para `AWS STS` (`AssumeRoleWithWebIdentity`) e Federação de Identidades Multi-Serviço.

## Fontes
- [CNCF Dex GitHub — README.md (Federated OpenID Connect Provider, ID Tokens, Kubernetes Authentication & Connectors Matrix)](https://raw.githubusercontent.com/dexidp/dex/master/README.md) — README oficial do dexidp/dex detalhando a emissão de ID Tokens JWT, integração com Kubernetes/AWS STS e matriz de estabilidade e recursos dos conectores; consultado em 2026-10-03.
- [CNCF Dex Official Documentation — Connectors Reference (Upstream IdP Protocol Translation, Refresh Token & Groups Support)](https://dexidp.io/docs/connectors/) — Documentação oficial de conectores do Dex cobrindo configuração de LDAP, GitHub, GitLab, OIDC e limitações de protocolo; consultado em 2026-10-03.
- [CNCF Dex — Official GitHub Repository](https://github.com/dexidp/dex) — Repositório oficial Apache-2.0 do CNCF Dex; consultado em 2026-10-03.
