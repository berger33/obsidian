---
id: software.seguranca.tranche12.001140
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

# Guia Definitivo de **Hardening e Monitoramento de AD CS (Blue Team)**: Ativando Auditoria da CA (**Event IDs `4886`, `4887`, `4888`, `4898`, `4899`**) e Regras Sigma

## Em uma frase
Um fato alarmante constatado em dezenas de respostas a incidentes reais é que, **por padrão no Windows Server, o serviço AD CS NÃO registra os logs detalhados de solicitação e emissão de certificados (`Event IDs 4886` e `4887`)** — a menos que o administrador ative tanto a política de auditoria do sistema operacional (`Audit Certification Services`) quanto a flag interna de auditoria da própria CA (`AuditFilter`)!

## Por que importa
Sem esses dois ajustes ativados, um invasor pode explorar `ESC1` ou `ESC8`, emitir um certificado de `Domain Admin` e o log de Segurança da CA ficará completamente em silêncio!

## Como funciona
Para ativar a visibilidade completa de AD CS no seu SOC: **(1)** Habilite via GPO em todos os servidores de CA a subcategoria **`Audit Certification Services` (Success and Failure)**; **(2)** Habilite todos os eventos de auditoria nas propriedades da CA executando **`certutil -setreg CA\AuditFilter 127`** e reiniciando o `CertSvc`; e **(3)** Configure os templates sensíveis para incluir o nome do solicitante no assunto ou audite os atributos da requisição no **Event ID `4886` (`Certificate Services received a certificate request`)** e **`4887` (`Certificate Services approved a certificate request and issued a certificate`)**!

## Exemplo
```powershell
# Comandos de Hardening e Ativacao de Auditoria Completa em um servidor Windows de Enterprise CA (AD CS)
auditpol /set /subcategory:"Certification Services" /success:enable /failure:enable
certutil -setreg CA\AuditFilter 127
certutil -setreg policy\EditFlags -EDITF_ATTRIBUTESUBJECTALTNAME2
Restart-Service CertSvc
```

## Limites e trade-offs
Com essa telemetria ativa e encaminhada ao seu SIEM (ou analisada com **Hayabusa** e **Chainsaw** usando as regras **Sigma `windows/builtin/security/` para AD CS**), monitore prioritariamente: **`EventID 4886/4887`** (emissão com SAN diferente do solicitante), **`EventID 4898`** (carregamento de template pela CA), **`EventID 4899`** (modificação de um Certificate Template), **`EventID 4870`** (revogação de certificado) e **`EventID 4876`** (backup da CA iniciado — alerta crítico de *Golden Certificate*!)!

## Como verificar
Execute `certipy find -vulnerable` mensalmente de forma automatizada e dispare um alerta caso qualquer item apareça sob `[!] Vulnerabilities`.

## Conexões
- [[certipy-persistencia-golden-certificates-roubo-chave-privada-ca-dpapi]] — Veja também: Persistência de Domínio com **Golden Certificates (`certipy ca -backup` / `certipy forge`)** e Como Proteger a Chave Privada da CA com **HSM**.
- [[certipy-arquitetura-auditoria-active-directory-certificate-services-adcs]] — Referência cruzada direta com certipy-arquitetura-auditoria-active-directory-certificate-services-adcs.
- [[certipy-enumeracao-find-vulnerable-bloodhound-templates-cas-ldap]] — Referência cruzada direta com certipy-enumeracao-find-vulnerable-bloodhound-templates-cas-ldap.
- [[hayabusa-deteccao-ataques-active-directory-dcsync-kerberoasting-golden-ticket]] — Referência cruzada direta com hayabusa-deteccao-ataques-active-directory-dcsync-kerberoasting-golden-ticket.

## Fontes
- [Certipy Official GitHub — Active Directory Certificate Services (AD CS) Attack & Enumeration Toolkit](https://raw.githubusercontent.com/ly4k/Certipy/main/README.md) — repositório oficial do Certipy cobrindo descoberta de CAs/Templates, identificação de vulnerabilidades ESC1–ESC17, Shadow Credentials e Golden Certificates; consultado em 2026-10-03.
- [Certipy Official Package & Architecture Specification (`pyproject.toml`)](https://raw.githubusercontent.com/ly4k/Certipy/main/pyproject.toml) — especificação técnica do pacote `certipy-ad` v5.1+ (`impacket`, `ldap3`, `cryptography`, `asn1crypto`, `neo4j`/BloodHound); consultado em 2026-10-03.
