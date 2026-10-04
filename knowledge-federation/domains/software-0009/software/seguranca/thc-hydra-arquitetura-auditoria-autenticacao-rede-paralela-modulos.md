---
id: software.seguranca.tranche16.001571
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-16.md"
fontes: ["https://raw.githubusercontent.com/vanhauser-thc/thc-hydra/master/README", "https://raw.githubusercontent.com/vanhauser-thc/thc-hydra/master/hydra.1"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Arquitetura do **THC-Hydra (`vanhauser-thc/thc-hydra`)**: Auditoria Paralelizada de Autenticação de Rede em Mais de 50 Protocolos (`SSH`, `RDP`, `SMB`, `HTTP-Form`, `LDAP`, `PostgreSQL`, `MySQL`, `SNMP`)

## Em uma frase
Enquanto o **Hashcat** e o **John the Ripper** testam milhões de hashes de senhas *Offline*, como testar em uma auditoria autorizada se serviços expostos na rede (**SSH, RDP, SMB, FTP, Telnet, HTTP/HTTPS Forms, PostgreSQL, MySQL, MS-SQL, Redis, LDAP, IMAP, SMTP, SNMP, VNC**) aceitam credenciais padrão de fábrica, senhas fracas ou sofrem ausência de *Account Lockout / Rate Limiting*?

## Por que importa
Usando o **THC-Hydra (`hydra`)**, criado por van Hauser (The Hacker's Choice) e documentado em `README` e na manpage `hydra(1)`!

## Como funciona
O Hydra é um motor em C altamente paralelizado que gerencia um pool de **Tasks de Conexão Simultâneas (`-t TASKS`, padrão `16`)** sobre mais de 50 protocolos de rede (com suporte nativo a SSL/TLS via `-S`), aceitando duas sintaxes de linha de comando: **(1) A sintaxe moderna baseada em URI**: `hydra [opções] protocolo://alvo:porta/opcoes_modulo` e **(2) A sintaxe clássica (obrigatória ao usar lista de servidores `-M alvos.txt`)**: `hydra [opções] -M alvos.txt protocolo [opcoes_modulo]`!

## Exemplo
```bash
# Inspecionar os protocolos compilados no binario do THC-Hydra e consultar as opcoes especificas de um modulo com hydra -U
hydra -h | head -n 25
hydra -U ssh
hydra -U http-post-form
```

## Limites e trade-offs
Veja na última linha acima a flag **`hydra -U <protocolo>`** documentada em `README` e `hydra(1)`: muitos módulos do Hydra possuem parâmetros opcionais ou obrigatórios específicos (por exemplo: o método de autenticação `NTLM` ou `PLAIN` no `smtp`, o `SID` no `oracle`, o banco de dados padrão no `postgres` ou a sintaxe de formulário no `http-post-form`); rodar `hydra -U <protocolo>` imprime a documentação exata daquele módulo!

## Como verificar
Lembre-se do aviso oficial no `README`: evite o protocolo `telnet` sempre que possível, pois banners de login Telnet não possuem código de retorno padronizado de protocolo e exigem correspondência textual manual.

## Conexões
- [[thc-hydra-modos-credenciais-password-spraying-u-colon-file-e-nsr]] — Veja também: Modos de Credenciais no THC-Hydra: **Password Spraying (`-u` Loop Around Users)**, Pares `login:pass` (**`-C`**), Verificações Extras (**`-e nsr`**) e Parada Imediata (**`-f` / `-F`**).
- [[thc-hydra-auditoria-formularios-web-http-post-form-get-form-cookies]] — Referência cruzada direta com thc-hydra-auditoria-formularios-web-http-post-form-get-form-cookies.

## Fontes
- [THC-Hydra Official Documentation (`vanhauser-thc/thc-hydra/master/README`)](https://raw.githubusercontent.com/vanhauser-thc/thc-hydra/master/README) — documentação oficial do THC-Hydra detalhando protocolos suportados, sintaxe URI `PROTOCOL://TARGET:PORT/OPTIONS`, listas `-M` e inspeção de módulos `hydra -U`; consultado em 2026-10-03.
- [Official `hydra(1)` Manpage Specification (`vanhauser-thc/thc-hydra/master/hydra.1`)](https://raw.githubusercontent.com/vanhauser-thc/thc-hydra/master/hydra.1) — manpage oficial `hydra(1)` detalhando flags `-l`/`-L`, `-p`/`-P`, `-C`, `-e nsr`, `-u`, `-f`/`-F`, `-t`/`-T`, `-w`/`-W`/`-c`, `-R`, `-b json` e o utilitário `pw-inspector`; consultado em 2026-10-03.
