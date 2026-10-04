---
id: software.seguranca.tranche12.001138
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

# Autenticação via Certificado com **`certipy auth`**: **Kerberos PKINIT (`EventID 4768`)**, **UnPAC-the-Hash (`PAC_CREDENTIAL_INFO`)** e **LDAPS Schannel**

## Em uma frase
Depois que um certificado `.pfx` é emitido (seja legitimamente ou através de um vetor `ESC1`–`ESC17`), como o **`certipy auth`** transforma esse arquivo `.pfx` em um Ticket-Granting Ticket (TGT) Kerberos (`.ccache`), recupera o **hash NTLM em texto claro da conta** ou abre um shell LDAP interativo?

## Por que importa
O comando **`certipy auth -pfx <arquivo.pfx>`** suporta dois protocolos de autenticação por certificado do Active Directory: **(1) Kerberos PKINIT (padrão)** — envia uma requisição `AS-REQ` assinada com o certificado para o KDC (porta `88`); o KDC responde com um `AS-REP` contendo o TGT e, porque a autenticação foi feita via PKINIT, inclui dentro do PAC (*Privilege Attribute Certificate*) a estrutura criptografada **`PAC_CREDENTIAL_INFO`** contendo o **hash NTLM (e chaves Kerberos) da conta**, que o Certipy descriptografa automaticamente usando a chave de sessão Diffie-Hellman/RSA (*técnica UnPAC-the-Hash*)!; e **(2) Schannel (`-ldap-shell`)** — quando o KDC não suporta PKINIT, o Certipy abre uma conexão TLS mútua (mTLS) diretamente na porta **`636` (LDAPS)** do Domain Controller usando o certificado cliente!

## Como funciona
No modo `-ldap-shell`, o operador pode modificar grupos, definir RBCD (`set_rbcd`) ou adicionar Shadow Credentials diretamente pela sessão LDAPS autenticada pelo certificado!

## Exemplo
```bash
# Testar autenticacao PKINIT em laboratorio com um certificado .pfx para verificar os eventos gerados no Domain Controller (Event ID 4768)
certipy auth \
  -pfx ./certificado_teste_auditoria.pfx \
  -dc-ip 10.10.10.5
```

## Limites e trade-offs
Como detectar **`certipy auth` (PKINIT e UnPAC-the-Hash)** nos logs do Domain Controller? **(1)** Para o **PKINIT**, monitore o **Event ID `4768`** (*A Kerberos authentication ticket (TGT) was requested*) onde os campos **`CertIssuerName`**, **`CertSerialNumber`** ou **`CertThumbprint`** estão preenchidos (`Pre-Authentication Type = 15` ou `16`); e **(2)** Para o **UnPAC-the-Hash**, monitore um **Event ID `4769`** (*A Kerberos service ticket was requested*) imediatamente subsequente onde uma conta solicita um ticket TGS **para si mesma** (`ServiceName` igual ao próprio `TargetUserName`) com cifra RC4/AES!

## Como verificar
Correlacione o `CertSerialNumber` do `EventID 4768` no DC com o log de emissão `EventID 4887` na CA para identificar exatamente quem solicitou aquele certificado.

## Conexões
- [[certipy-shadow-credentials-msds-keycredentiallink-whfb-pkinit]] — Veja também: Auditoria e Abuso de **Shadow Credentials (`msDS-KeyCredentialLink`)** com **`certipy shadow`**: Como Funciona o **Windows Hello for Business (WHfB)** no AD.
- [[certipy-persistencia-golden-certificates-roubo-chave-privada-ca-dpapi]] — Veja também: Persistência de Domínio com **Golden Certificates (`certipy ca -backup` / `certipy forge`)** e Como Proteger a Chave Privada da CA com **HSM**.
- [[certipy-arquitetura-auditoria-active-directory-certificate-services-adcs]] — Referência cruzada direta com certipy-arquitetura-auditoria-active-directory-certificate-services-adcs.
- [[certipy-vulnerabilidades-templates-esc1-esc2-esc3-san-eku-enrollment]] — Referência cruzada direta com certipy-vulnerabilidades-templates-esc1-esc2-esc3-san-eku-enrollment.
- [[hayabusa-deteccao-ataques-active-directory-dcsync-kerberoasting-golden-ticket]] — Referência cruzada direta com hayabusa-deteccao-ataques-active-directory-dcsync-kerberoasting-golden-ticket.

## Fontes
- [Certipy Official GitHub — Active Directory Certificate Services (AD CS) Attack & Enumeration Toolkit](https://raw.githubusercontent.com/ly4k/Certipy/main/README.md) — repositório oficial do Certipy cobrindo descoberta de CAs/Templates, identificação de vulnerabilidades ESC1–ESC17, Shadow Credentials e Golden Certificates; consultado em 2026-10-03.
- [Certipy Official Package & Architecture Specification (`pyproject.toml`)](https://raw.githubusercontent.com/ly4k/Certipy/main/pyproject.toml) — especificação técnica do pacote `certipy-ad` v5.1+ (`impacket`, `ldap3`, `cryptography`, `asn1crypto`, `neo4j`/BloodHound); consultado em 2026-10-03.
