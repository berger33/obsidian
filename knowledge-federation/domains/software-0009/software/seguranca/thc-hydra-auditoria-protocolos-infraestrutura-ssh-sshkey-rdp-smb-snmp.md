---
id: software.seguranca.tranche16.001576
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

# Auditando Protocolos de Infraestrutura e Gerência no THC-Hydra: **`ssh` / `sshkey`**, **`rdp`**, **`smb`**, **`snmp` (Community Strings v1/v2c/v3)** e **`cisco-enable`**

## Em uma frase
Além de senhas de usuário em SSH, RDP e SMB, você sabia que o **THC-Hydra** possui módulos dedicados para auditar **Chaves Privadas SSH Pré-Conhecidas (`sshkey`)**, **Community Strings de Gerência `SNMP` (`snmp` v1, v2c e v3)** e senhas de modo privilegiado de equipamentos de rede (**`cisco`** e **`cisco-enable`**)?

## Por que importa
Veja dois casos de uso de altíssimo impacto em auditorias de infraestrutura: **(1) Auditoria de `SNMP Community Strings` (`snmp` na porta `161/udp`)** — muitos switches, roteadores, no-breaks (UPS) e impressoras saem de fábrica com as *Community Strings* padrão **`public` (leitura)** e **`private` (leitura e escrita da configuração inteira do roteador via SNMP!)** habilitadas!

## Como funciona
**(2) Módulo `smb`** — permite especificar via opção de módulo `-m` se a conta deve ser autenticada como conta Local (`-m Local`), de Domínio (`-m Domain`) ou passando diretamente hashes **NTLM (`-m Hash`)**!

## Exemplo
```bash
# Auditar Community Strings SNMP (v2c) em switches/equipamentos de rede e verificar opcoes do modulo SMB no THC-Hydra
hydra -P ./snmp_communities_padrao.txt -f -t 4 snmp://192.0.2.1/2c
hydra -U smb
```

## Limites e trade-offs
Olhe na primeira linha acima (`snmp://192.0.2.1/2c`): no módulo `snmp` do Hydra, como nas versões `SNMPv1` e `SNMPv2c` não existe "nome de usuário" (apenas a *Community String*), você passa a lista de communities candidatas com **`-P`** (como `public`, `private`, `manager`, `cisco`, `monitor`) e pode especificar a versão do protocolo (`1`, `2c` ou `3`) e o modo (`READ` ou `WRITE`) nas opções do módulo (`hydra -U snmp`)!

## Como verificar
Como mitigar 100% os riscos de SNMP nos seus switches e servidores Linux? Desative `SNMPv1` e `SNMPv2c` (que trafegam a *Community String* em texto claro em cada pacote UDP!) e migre exclusivamente para **`SNMPv3` em modo `authPriv` (autenticação `SHA-256` + criptografia `AES`)**!

## Conexões
- [[thc-hydra-auditoria-bancos-dados-postgres-mysql-mssql-redis-mongodb]] — Veja também: Auditando Autenticação de Bancos de Dados (**PostgreSQL, MySQL/MariaDB, MS-SQL, Redis, MongoDB e Oracle**) com o THC-Hydra.
- [[thc-hydra-geracao-bruteforce-x-charset-pw-inspector-filtragem-wordlists]] — Veja também: Geração On-the-Fly (**`-x min:max:charset`**) e Filtragem de Wordlists por Política de Senha com o Utilitário **`pw-inspector`** do THC-Hydra.
- [[thc-hydra-arquitetura-auditoria-autenticacao-rede-paralela-modulos]] — Referência cruzada direta com thc-hydra-arquitetura-auditoria-autenticacao-rede-paralela-modulos.
- [[thc-hydra-modos-credenciais-password-spraying-u-colon-file-e-nsr]] — Referência cruzada direta com thc-hydra-modos-credenciais-password-spraying-u-colon-file-e-nsr.

## Fontes
- [THC-Hydra Official Documentation (`vanhauser-thc/thc-hydra/master/README`)](https://raw.githubusercontent.com/vanhauser-thc/thc-hydra/master/README) — documentação oficial do THC-Hydra detalhando protocolos suportados, sintaxe URI `PROTOCOL://TARGET:PORT/OPTIONS`, listas `-M` e inspeção de módulos `hydra -U`; consultado em 2026-10-03.
- [Official `hydra(1)` Manpage Specification (`vanhauser-thc/thc-hydra/master/hydra.1`)](https://raw.githubusercontent.com/vanhauser-thc/thc-hydra/master/hydra.1) — manpage oficial `hydra(1)` detalhando flags `-l`/`-L`, `-p`/`-P`, `-C`, `-e nsr`, `-u`, `-f`/`-F`, `-t`/`-T`, `-w`/`-W`/`-c`, `-R`, `-b json` e o utilitário `pw-inspector`; consultado em 2026-10-03.
