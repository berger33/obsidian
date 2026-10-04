---
id: software.seguranca.tranche12.001132
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

# Enumeração e Diagnóstico de AD CS com **`certipy find`**: Flag **`-vulnerable`**, Saída JSON/Stdout e Integração com **BloodHound**

## Em uma frase
Como descobrir em menos de 30 segundos se algum dos dezenas de *Certificate Templates* publicados nas suas Enterprise CAs do Active Directory permite que um usuário comum do domínio emita um certificado em nome de um `Domain Admin`?

## Por que importa
O subcomando **`certipy find`** conecta-se ao Domain Controller via LDAP/LDAPS, enumera todas as **Enterprise Certificate Authorities** (no container `CN=Public Key Services,CN=Services,CN=Configuration,DC=...`), todos os **Certificate Templates** habilitados, as **ACLs de permissão (`Enroll`, `Autoenroll`, `WriteOwner`, `WriteDacl`, `WriteProperty`)**, configurações de registro da CA via RPC e endpoints HTTP de Web Enrollment!

## Como funciona
Ao passar as flags **`-vulnerable`** e **`-stdout`** (ou inspecionar o arquivo `.json` / `.txt` gerado com o prefixo de timestamp), o Certipy filtra e exibe na seção **`[!] Vulnerabilities`** exatamente qual código **`ESC1`–`ESC17`** afeta cada CA ou Template e quais grupos do AD (ex.: `Domain Users`, `Authenticated Users`, `Domain Computers`) possuem direitos de exploração!

## Exemplo
```bash
# Executar uma auditoria defensiva de leitura no AD CS para listar apenas as vulnerabilidades (ESC1-ESC17) encontradas no dominio
certipy find \
  -u 'auditor@corp.interno' \
  -p 'SenhaSeguraDeAuditoria!' \
  -dc-ip 10.10.10.5 \
  -vulnerable -stdout
```

## Limites e trade-offs
Além do relatório em texto e JSON, o `certipy find` gera um arquivo `.zip` pronto para ser arrastado para dentro do **BloodHound** (ou **BloodHound CE / OpenGraph**), permitindo cruzar permissões de grupos do AD com templates AD CS vulneráveis em consultas Cypher de caminhos de ataque!

## Como verificar
Se a sua estação de auditoria já possui um ticket Kerberos ativo (`KRB5CCNAME`), passe a flag `-k -no-pass` ao `certipy find` para autenticar via Kerberos sem trafegar senhas ou hashes NTLM.

## Conexões
- [[certipy-arquitetura-auditoria-active-directory-certificate-services-adcs]] — Veja também: Arquitetura do **Certipy (`ly4k/Certipy`)**: Auditoria, Enumeração e Testes de Segurança em **Active Directory Certificate Services (AD CS)**.
- [[certipy-vulnerabilidades-templates-esc1-esc2-esc3-san-eku-enrollment]] — Veja também: Anatomia e Mitigação de **`ESC1`, `ESC2` e `ESC3`**: Abuso de **`ENROLLEE_SUPPLIES_SUBJECT` (SAN)**, **Any Purpose EKU** e **Enrollment Agent**.
- [[certipy-permissoes-acls-esc4-esc5-esc7-writeproperty-manageca]] — Referência cruzada direta com certipy-permissoes-acls-esc4-esc5-esc7-writeproperty-manageca.

## Fontes
- [Certipy Official GitHub — Active Directory Certificate Services (AD CS) Attack & Enumeration Toolkit](https://raw.githubusercontent.com/ly4k/Certipy/main/README.md) — repositório oficial do Certipy cobrindo descoberta de CAs/Templates, identificação de vulnerabilidades ESC1–ESC17, Shadow Credentials e Golden Certificates; consultado em 2026-10-03.
- [Certipy Official Package & Architecture Specification (`pyproject.toml`)](https://raw.githubusercontent.com/ly4k/Certipy/main/pyproject.toml) — especificação técnica do pacote `certipy-ad` v5.1+ (`impacket`, `ldap3`, `cryptography`, `asn1crypto`, `neo4j`/BloodHound); consultado em 2026-10-03.
