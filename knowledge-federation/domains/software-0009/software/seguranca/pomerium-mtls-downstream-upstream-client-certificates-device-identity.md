---
id: software.seguranca.tranche03.000244
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
fontes: ["https://www.pomerium.com/docs", "https://raw.githubusercontent.com/pomerium/pomerium/main/README.md", "https://github.com/pomerium/pomerium"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Pomerium `mTLS` Downstream (Certificados de Cliente/Dispositivo) e Upstream (Criptografia Mútua Proxy -> Backend)

## Em uma frase
O Pomerium suporta **Mutual TLS (mTLS)** em ambas as pontas da conexão: 1) **Downstream mTLS** (entre o navegador/dispositivo do usuário e o Pomerium, usando `downstream_mtls` para exigir um certificado X.509 de cliente emitido pela PKI de dispositivos da empresa além do login OIDC); e 2) **Upstream mTLS** (entre o Pomerium Proxy e o serviço interno de destino, usando `tls_client_cert_file` / `tls_custom_ca_file`).

## Por que importa
Em uma arquitetura Zero Trust rigorosa (BeyondCorp), possuir apenas o login/senha e MFA do usuário não garante que o acesso esteja partindo de um laptop corporativo gerenciado (MDM); exigir um certificado de cliente de dispositivo em `downstream_mtls` bloqueia o acesso a partir de computadores pessoais não gerenciados.

## Como funciona
Com `downstream_mtls.enforcement: policy` (ou `reject_connection`), você pode usar critérios de certificado de cliente diretamente dentro da política PPL (como **`invalid_client_certificate`**) para exigir certificado de dispositivo apenas nas rotas mais críticas de produção!

## Exemplo
```yaml
downstream_mtls:
  ca_file: /etc/pomerium/certs/device-fleet-ca.pem
  enforcement: policy

routes:
  - from: https://prod-db-admin.internal.corp
    to: https://db-admin.internal.svc.cluster.local:8443
    tls_custom_ca_file: /etc/pomerium/certs/internal-service-ca.pem
    tls_client_cert_file: /etc/pomerium/certs/pomerium-client.crt
    tls_client_key_file: /etc/pomerium/certs/pomerium-client.key
    policy:
      - allow:
          and:
            - domain:
                is: internal.corp
      - deny:
          or:
            - invalid_client_certificate: true
```

## Limites e trade-offs
Ao configurar `downstream_mtls.crl_file` (ou validação de revogação), o Pomerium rejeita imediatamente certificados de laptops corporativos que foram reportados como perdidos ou roubados.

## Como verificar
Teste o acesso à rota com e sem o certificado de cliente instalado (`curl --cert client.crt --key client.key ...`).

## Conexões
- [[pomerium-jwt-assertion-header-x-pomerium-jwt-assertion-verificacao-upstream]] — Veja também: Pomerium Identity Propagation (`X-Pomerium-Jwt-Assertion`): assinatura criptográfica da identidade do usuário para a aplicação backend.
- [[pomerium-acesso-tcp-ssh-rdp-postgres-tunelamento-autenticado]] — Veja também: Pomerium Rotas `TCP` (`tcp+https://`): acesso Zero-Trust a bancos de dados (`PostgreSQL`, `Redis`), `SSH` e `RDP` sem VPN.

## Fontes
- [Pomerium Official Documentation — What is Pomerium? (BeyondCorp Zero-Trust Access Proxy, Authenticate/Authorize/Proxy Flow & Core Architecture)](https://www.pomerium.com/docs) — Documentação oficial do Pomerium explicando o modelo de acesso sem cliente baseado em identidade, dispositivo e contexto por requisição; consultado em 2026-10-03.
- [Pomerium GitHub — README.md (Identity and Context-Aware Reverse Proxy, Clientless Access & Continuous Verification)](https://raw.githubusercontent.com/pomerium/pomerium/main/README.md) — README oficial do pomerium/pomerium apresentando a arquitetura do proxy reverso Zero-Trust em Go e Envoy; consultado em 2026-10-03.
- [Pomerium — Official GitHub Repository](https://github.com/pomerium/pomerium) — Repositório oficial Apache-2.0 do Pomerium; consultado em 2026-10-03.
