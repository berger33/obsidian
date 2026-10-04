---
id: software.seguranca.tranche14.001384
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-14.md"
fontes: ["https://raw.githubusercontent.com/freeipa/freeipa/master/README.md", "https://raw.githubusercontent.com/freeipa/freeipa/master/BUILD.txt"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# PKI Corporativa Integrada (**Dogtag CA & KRA**) e Renovação Automática de Certificados em Hosts Linux com **`certmonger` (`ipa-getcert`)** no FreeIPA

## Em uma frase
Como emitir e renovar automaticamente certificados X.509 mTLS para centenas de servidores internos (Nginx, Apache, PostgreSQL, Cockpit, LDAPS, RabbitMQ, Prometheus) em uma frota Linux sem precisar copiar arquivos `.pem` na mão e sem risco de um certificado expirar num domingo de madrugada?

## Por que importa
O **FreeIPA** incorpora nativamente a **Dogtag PKI** (Autoridade Certificadora completa compatível com **ACME**, perfis customizados de certificado, **Sub-CAs**, **OCSP Responder** e **KRA — *Key Recovery Authority*/Vault** para guarda segura de chaves assimétricas/simétricas!) e, no lado de cada servidor Linux cliente, trabalha em conjunto com o daemon **`certmonger` (`ipa-getcert`)**!

## Como funciona
Quando você solicita um certificado em qualquer máquina do domínio usando **`ipa-getcert request`**, o `certmonger`: **(1)** Gera o par de chaves localmente na máquina, **(2)** Autentica no FreeIPA usando o ticket Kerberos da própria máquina (`host/srv01.exemplo.br@EXEMPLO.BR`), **(3)** Obtém o certificado assinado pela Dogtag CA do FreeIPA, **(4)** Salva em `/etc/pki/...` e **(5) Monitora o vencimento diariamente, renovando o certificado sozinho antes de expirar e recarregando o serviço (`-C "systemctl reload nginx"`)**!

## Exemplo
```bash
# Solicitar em um servidor membro do FreeIPA um certificado TLS assinado pela CA corporativa com auto-renovacao gerenciada pelo certmonger (ipa-getcert)
ipa service-add HTTP/$(hostname -f)
ipa-getcert request \
  -f /etc/pki/tls/certs/app-interna.crt \
  -k /etc/pki/tls/private/app-interna.key \
  -K HTTP/$(hostname -f) \
  -D $(hostname -f) \
  -C "systemctl reload nginx"
ipa-getcert list
```

## Limites e trade-offs
Além do `certmonger` nativo via XML-RPC/Kerberos, as versões modernas do FreeIPA também incluem um **Servidor ACME Integrado (`ipa-acme-manage enable`)** na Dogtag PKI: isso significa que até aplicações, roteadores ou clusters Kubernetes (`cert-manager`) que não possuem o cliente FreeIPA instalado podem emitir certificados internos automaticamente via protocolo **ACME (`RFC 8555`)**!

## Como verificar
Ao instalar o FreeIPA em ambientes corporativos que já possuem uma CA Raiz Offline existente (ex.: Microsoft AD CS ou HSM Offline), use **`ipa-server-install --external-ca`** para que a CA do FreeIPA seja instalada como uma **CA Subordinada (Intermediate CA)** assinada pela sua Raiz corporativa!

## Conexões
- [[freeipa-governanca-sudo-centralizado-sudorule-sudocmd-auditoria]] — Veja também: Governança Centralizada de **`sudo` (`sudorule`, `sudocmd`, `sudocmdgroup`)** no FreeIPA: Aposentando arquivos `/etc/sudoers` Locais Espalhados.
- [[freeipa-autenticacao-2fa-otp-totp-hotp-passkeys-radius-pkinit]] — Veja também: Autenticação Multifator (**2FA / MFA**) e **Passwordless** no FreeIPA: Tokens **TOTP/HOTP (`otptoken`)**, **Passkeys FIDO2**, **Smartcards (`PKINIT`)** e **RADIUS Proxy**.
- [[freeipa-arquitetura-identidade-linux-389ds-kerberos-dogtag-pki-dns]] — Referência cruzada direta com freeipa-arquitetura-identidade-linux-389ds-kerberos-dogtag-pki-dns.
- [[rustls-validacao-certificados-webpki-root-store-pinning-crl]] — Referência cruzada direta com rustls-validacao-certificados-webpki-root-store-pinning-crl.
- [[openssl-operacoes-pki-ca-x509-req-crl-ocsp-automacao]] — Referência cruzada direta com openssl-operacoes-pki-ca-x509-req-crl-ocsp-automacao.

## Fontes
- [FreeIPA Official GitHub Repository (`freeipa/freeipa`)](https://raw.githubusercontent.com/freeipa/freeipa/master/README.md) — repositório oficial do projeto FreeIPA cobrindo integração de 389 Directory Server, MIT Kerberos, Dogtag PKI, BIND DNS, SSSD, HBAC, Sudo e Active Directory Trusts; consultado em 2026-10-03.
- [FreeIPA Official Build & Management Architecture Guide (`BUILD.txt`)](https://raw.githubusercontent.com/freeipa/freeipa/master/BUILD.txt) — documentação técnica oficial do FreeIPA detalhando `ipa-server-install`, autenticação Kerberos (`kinit admin`), framework de gerenciamento CLI/WebUI (`ipa`) e validação de API; consultado em 2026-10-03.
