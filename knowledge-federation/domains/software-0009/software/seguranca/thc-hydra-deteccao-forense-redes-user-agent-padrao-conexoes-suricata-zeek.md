---
id: software.seguranca.tranche16.001580
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

# Engenharia de Detecção (**Blue Team / SOC / NIDS / SIEM**) Contra Ataques do **THC-Hydra**: `User-Agent` Default (`Mozilla/4.0 (Hydra)`), Padrões de Conexão e Correlação

## Em uma frase
Como os sensores de rede (**Suricata / Cisco Snort 3 / Zeek**) e o SIEM (**Wazuh / Sigma / Hayabusa**) detectam instantaneamente que alguém está executando o **THC-Hydra** contra aplicações web, servidores SSH, RDP ou bancos de dados da organização?

## Por que importa
Existem **3 assinaturas clássicas e comportamentais** que todo analista de SOC deve conhecer: **(1) Cabeçalho HTTP `User-Agent` Padrão do Hydra** — nos módulos `http-*` e `https-*`, se o operador não sobrescrever o `User-Agent` manualmente na opção `H=User-Agent: ...`, o Hydra envia por padrão o cabeçalho literal **`User-Agent: Mozilla/4.0 (Hydra)`** (que todas as regras de **OWASP CRS v4 (`913100`)**, **Suricata** e **Snort 3** detectam no primeiro pacote!).

## Como funciona
**(2) Burst de Conexões Paralelas Curtas na Mesma Porta (`-t 16` default)** — no Zeek (`conn.log`, `ssh.log`, `rdp.log`), 16 conexões TCP simultâneas vindas do mesmo IP de origem com duração `< 1s` e `auth_success = F` para o mesmo serviço; e **(3) Tentativas de `Password Spraying` (`-u`)** — eventos `4625` (Windows) ou `pam_unix authentication failure` (Linux) distribuídos sequencialmente em dezenas de nomes de usuários distintos a partir do mesmo IP!

## Exemplo
```bash
# Pesquisar em logs de acesso HTTP ou alertas do Suricata/Zeek pelo User-Agent padrao do THC-Hydra e por rajadas de falhas de autenticacao
grep -i "Mozilla/4.0 (Hydra)" /var/log/nginx/access.log
```

## Limites e trade-offs
Olhe como a defesa em profundidade neutraliza completamente ataques automatizados de força bruta e *Password Spraying*: **(1)** Desative autenticação por senha no SSH (`PasswordAuthentication no`, permitindo apenas chaves públicas/certificados/FIDO2 `-sk`); **(2)** Exija **MFA Resistente a Phishing (`FIDO2 / WebAuthn`)** em todos os portais web e VPNs; **(3)** Aplique **`pam_faillock`** e bloqueio de IP dinâmico (**Fail2ban / CrowdSec**); e **(4)** Audite regularmente suas senhas internas com **John the Ripper / Hashcat**!

## Como verificar
Com isso fechamos o módulo do **THC-Hydra** na Tranche 16!

## Conexões
- [[thc-hydra-validacao-controles-defensivos-fail2ban-crowdsec-waf-pam]] — Veja também: Usando o THC-Hydra em **Purple Team e Engenharia de Confiabilidade de Segurança** para Validar Regras do **Fail2ban, CrowdSec, WAF (Coraza/ModSecurity) e `pam_faillock`**.
- [[thc-hydra-arquitetura-auditoria-autenticacao-rede-paralela-modulos]] — Referência cruzada direta com thc-hydra-arquitetura-auditoria-autenticacao-rede-paralela-modulos.

## Fontes
- [THC-Hydra Official Documentation (`vanhauser-thc/thc-hydra/master/README`)](https://raw.githubusercontent.com/vanhauser-thc/thc-hydra/master/README) — documentação oficial do THC-Hydra detalhando protocolos suportados, sintaxe URI `PROTOCOL://TARGET:PORT/OPTIONS`, listas `-M` e inspeção de módulos `hydra -U`; consultado em 2026-10-03.
- [Official `hydra(1)` Manpage Specification (`vanhauser-thc/thc-hydra/master/hydra.1`)](https://raw.githubusercontent.com/vanhauser-thc/thc-hydra/master/hydra.1) — manpage oficial `hydra(1)` detalhando flags `-l`/`-L`, `-p`/`-P`, `-C`, `-e nsr`, `-u`, `-f`/`-F`, `-t`/`-T`, `-w`/`-W`/`-c`, `-R`, `-b json` e o utilitário `pw-inspector`; consultado em 2026-10-03.
