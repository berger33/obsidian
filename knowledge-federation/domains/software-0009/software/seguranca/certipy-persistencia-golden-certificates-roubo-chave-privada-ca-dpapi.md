---
id: software.seguranca.tranche12.001139
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-12.md"
fontes: ["https://raw.githubusercontent.com/ly4k/Certipy/main/README.md", "https://raw.githubusercontent.com/ly4k/Certipy/main/pyproject.toml"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Persistência de Domínio com **Golden Certificates (`certipy ca -backup` / `certipy forge`)** e Como Proteger a Chave Privada da CA com **HSM**

## Em uma frase
Todos os analistas de segurança conhecem o *Golden Ticket* do Kerberos (onde o atacante rouba o hash da conta `krbtgt` para forjar TGTs), mas o Active Directory possui um equivalente em PKI ainda mais persistente: o **Golden Certificate**!

## Por que importa
Por padrão, quando o serviço **AD CS** é instalado no Windows Server sem um **Hardware Security Module (HSM)** dedicado, a **chave privada raiz da Autoridade Certificadora (CA)** fica armazenada no próprio servidor da CA (protegida pelo Microsoft Software Key Storage Provider / DPAPI do sistema)! Se um atacante comprometer o servidor da CA, ele pode executar **`certipy ca -backup`** para extrair o certificado e a chave privada da CA (`.pfx`)!

## Como funciona
De posse do `.pfx` da CA, o atacante pode rodar **`certipy forge -ca-pfx ca.pfx -upn administrator@corp.interno`** em sua própria máquina **completamente offline**, forjando certificados válidos para qualquer usuário ou Domain Controller da floresta! E o pior: **trocar a senha da conta `Administrator` ou mesmo trocar duas vezes a senha da conta `krbtgt` NÃO invalida um Golden Certificate** — porque o certificado forjado é criptograficamente assinado pela CA confiável no container `NTAuthCertificates` do AD!

## Exemplo
```bash
# Auditar nas propriedades da CA (via JSON do certipy find ou certutil) qual Provider (CSP/KSP) protege a chave privada da CA
certutil -store My
```

## Limites e trade-offs
Como proteger sua infraestrutura contra **Golden Certificates**? **(1)** Armazene a chave privada das suas Root CAs (offline!) e Enterprise Issuing CAs dentro de um **Hardware Security Module (HSM) certificado FIPS 140-3** (onde a chave privada é fisicamente não-exportável); **(2)** Trate o servidor da Enterprise CA como **Tier 0** (com a mesma proteção de um Domain Controller, sem acesso de administradores de servidores comuns); e **(3)** Se uma CA baseada em software for comprometida, a única erradicação completa é **revogar e remover o certificado daquela CA comprometida do objeto `CN=NTAuthCertificates` e `CN=AIA` no Active Directory e descomissionar a CA**!

## Como verificar
Ative auditoria de exportação de chaves privadas e monitore acessos ao armazenamento de chaves da máquina (`C:\ProgramData\Microsoft\Crypto\RSA\MachineKeys\`).

## Conexões
- [[certipy-autenticacao-pkinit-schannel-certipy-auth-unpac-the-hash]] — Veja também: Autenticação via Certificado com **`certipy auth`**: **Kerberos PKINIT (`EventID 4768`)**, **UnPAC-the-Hash (`PAC_CREDENTIAL_INFO`)** e **LDAPS Schannel**.
- [[certipy-hardening-monitoramento-adcs-event-ids-4886-4887-sigma]] — Veja também: Guia Definitivo de **Hardening e Monitoramento de AD CS (Blue Team)**: Ativando Auditoria da CA (**Event IDs `4886`, `4887`, `4888`, `4898`, `4899`**) e Regras Sigma.
- [[certipy-arquitetura-auditoria-active-directory-certificate-services-adcs]] — Referência cruzada direta com certipy-arquitetura-auditoria-active-directory-certificate-services-adcs.
- [[certipy-permissoes-acls-esc4-esc5-esc7-writeproperty-manageca]] — Referência cruzada direta com certipy-permissoes-acls-esc4-esc5-esc7-writeproperty-manageca.

## Fontes
- [Certipy Official GitHub — Active Directory Certificate Services (AD CS) Attack & Enumeration Toolkit](https://raw.githubusercontent.com/ly4k/Certipy/main/README.md) — repositório oficial do Certipy cobrindo descoberta de CAs/Templates, identificação de vulnerabilidades ESC1–ESC17, Shadow Credentials e Golden Certificates; consultado em 2026-10-03.
- [Certipy Official Package & Architecture Specification (`pyproject.toml`)](https://raw.githubusercontent.com/ly4k/Certipy/main/pyproject.toml) — especificação técnica do pacote `certipy-ad` v5.1+ (`impacket`, `ldap3`, `cryptography`, `asn1crypto`, `neo4j`/BloodHound); consultado em 2026-10-03.
