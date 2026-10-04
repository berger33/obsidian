---
id: software.seguranca.tranche12.001135
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

# Configurações Inseguras da CA e **NTLM Relay para AD CS (`ESC6`, `ESC8` e `ESC11`)**: Flag `EDITF_ATTRIBUTESUBJECTALTNAME2`, Web Enrollment HTTP e RPC

## Em uma frase
Mesmo que todos os seus templates e ACLs estejam perfeitos, duas configurações em nível de servidor na Autoridade Certificadora abrem caminhos críticos de comprometimento de domínio que o Certipy detecta automaticamente como **`ESC6`**, **`ESC8`** e **`ESC11`**!

## Por que importa
**`ESC6`** ocorre quando o administrador da CA executou no passado `certutil -setreg policy\EditFlags +EDITF_ATTRIBUTESUBJECTALTNAME2`: essa única flag global faz a CA aceitar um **SAN (`Subject Alternative Name`) arbitrário especificado nos atributos de requisição de QUALQUER template** (como o template padrão `User` ou `Machine`), mesmo que o template não tenha `ENROLLEE_SUPPLIES_SUBJECT` habilitado (mitigado pelos patches de `SidExtension` de maio de 2022 `CVE-2022-26923`, mas ainda crítico se o mapeamento forte de certificados não estiver em modo *Enforcement*)!

## Como funciona
Já **`ESC8`** e **`ESC11`** são vetores de **NTLM Relay (`certipy relay`)**: **`ESC8`** ocorre quando o serviço IIS de **AD CS Web Enrollment (`/certsrv/`)** ou **CES/CEP** está habilitado sobre HTTP sem **Extended Protection for Authentication (EPA)** e sem HTTPS obrigatório, permitindo que um atacante coagindo uma máquina (ex.: Domain Controller via `PetitPotam` / `PrinterBug`) faça relay da autenticação NTLM para `http://<ca>/certsrv/certfnsh.asp` e emita um certificado daquele DC; e **`ESC11`** faz o mesmo relay NTLM diretamente contra a interface RPC (`ICertPassage` / `IF_NOREMOTEICERTREQUESTENCRYPTED` desabilitado) da CA!

## Exemplo
```bash
# Verificar no relatorio do certipy find se Web Enrollment (ESC8), User Specified SAN (ESC6) ou RPC sem criptografia (ESC11) estao ativos na CA
jq '.["Certificate Authorities"] | to_entries[] | {
  ca: .value["CA Name"],
  user_specified_san_esc6: .value["User Specified SAN"],
  web_enrollment_esc8: .value["Web Enrollment"],
  enforce_encrypt_icertrequest_esc11: .value["Enforce Encryption for Requests"]
}' ./*_Certipy.json
```

## Limites e trade-offs
Como blindar a sua CA contra **`ESC6`, `ESC8` e `ESC11`** hoje mesmo? **(1)** Desative imediatamente a flag `EDITF_ATTRIBUTESUBJECTALTNAME2` (`certutil -setreg policy\EditFlags -EDITF_ATTRIBUTESUBJECTALTNAME2` e reinicie o serviço `CertSvc`); **(2)** Se não precisar do Web Enrollment legado `/certsrv/`, desinstale a role IIS `AD CS Web Enrollment`; se precisar, exija **HTTPS (SSL)** e ative **Extended Protection for Authentication (`EPA = Require`)** no IIS; e **(3)** Certifique-se de que `IF_ENFORCEENCRYPTICERTREQUEST` está ativo na interface RPC da CA!

## Como verificar
Bloqueie também protocolos de coerção NTLM desnecessários (como o serviço `Spooler` de impressão em Domain Controllers e servidores Tier 0).

## Conexões
- [[certipy-permissoes-acls-esc4-esc5-esc7-writeproperty-manageca]] — Veja também: Controle de Acesso no AD CS (**`ESC4`, `ESC5` e `ESC7`**): ACLs Perigosas em Templates (`certipy template`) e na Autoridade Certificadora (`ManageCA` / `ManageCertificates`).
- [[certipy-mapeamento-certificados-esc9-esc10-esc13-esc14-esc15-kb5014754]] — Veja também: Mapeamento Fraco de Certificados e Novas Classes (**`ESC9`, `ESC10`, `ESC13`, `ESC14`, `ESC15`/`EKUwu`, `ESC16` e `ESC17`**) e o Patch **`KB5014754`**.
- [[certipy-arquitetura-auditoria-active-directory-certificate-services-adcs]] — Referência cruzada direta com certipy-arquitetura-auditoria-active-directory-certificate-services-adcs.
- [[certipy-enumeracao-find-vulnerable-bloodhound-templates-cas-ldap]] — Referência cruzada direta com certipy-enumeracao-find-vulnerable-bloodhound-templates-cas-ldap.

## Fontes
- [Certipy Official GitHub — Active Directory Certificate Services (AD CS) Attack & Enumeration Toolkit](https://raw.githubusercontent.com/ly4k/Certipy/main/README.md) — repositório oficial do Certipy cobrindo descoberta de CAs/Templates, identificação de vulnerabilidades ESC1–ESC17, Shadow Credentials e Golden Certificates; consultado em 2026-10-03.
- [Certipy Official Package & Architecture Specification (`pyproject.toml`)](https://raw.githubusercontent.com/ly4k/Certipy/main/pyproject.toml) — especificação técnica do pacote `certipy-ad` v5.1+ (`impacket`, `ldap3`, `cryptography`, `asn1crypto`, `neo4j`/BloodHound); consultado em 2026-10-03.
