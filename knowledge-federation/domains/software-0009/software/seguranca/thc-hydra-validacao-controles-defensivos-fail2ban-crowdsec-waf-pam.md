---
id: software.seguranca.tranche16.001579
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

# Usando o THC-Hydra em **Purple Team e Engenharia de Confiabilidade de Segurança** para Validar Regras do **Fail2ban, CrowdSec, WAF (Coraza/ModSecurity) e `pam_faillock`**

## Em uma frase
Qual é o caso de uso mais frequente do **THC-Hydra** no dia a dia de engenheiros de DevSecOps, administradores Linux e equipes de **Purple Team**? **Testar e comprovar matematicamente que os controles de defesa contra força bruta (`Fail2ban`, `CrowdSec`, `pam_faillock`, `Rate Limiting` do Nginx/Envoy/Vaultwarden e regras do `OWASP CRS v4`) estão realmente bloqueando o atacante dentro do SLA esperado!**

## Por que importa
Imagine que você acabou de configurar uma jail `[sshd]` no **Fail2ban** (`maxretry = 5`, `findtime = 10m`) ou um cenário `ssh-bf` no **CrowdSec**, ou o `pam_faillock` (`deny = 5`). Como ter certeza absoluta de que o bloqueio funciona na prática?

## Como funciona
Você dispara a partir de um host de teste autorizado um comando controlado do **THC-Hydra** com **`-l usuario_teste_canary -P 10_senhas_invalidas.txt -t 1 -V`** e verifica: **(1)** Se na 5ª tentativa o IP do scanner é banido no `nftables`/`iptables` pelo Fail2ban/CrowdSec; **(2)** Se a conta entra em lockout no `faillock --user usuario_teste_canary`; e **(3)** Se o alerta chega no SIEM (**Wazuh / Suricata / Snort 3**)!

## Exemplo
```bash
# Disparar 6 tentativas sequenciais controladas (-t 1 -W 1 -V) contra um servico de homologacao para validar o disparo automatico do Fail2ban / pam_faillock
hydra -l canario_auditoria -P ./6_tentativas_teste.txt -t 1 -W 1 -V ssh://192.0.2.10:22
faillock --user canario_auditoria
fail2ban-client status sshd
```

## Limites e trade-offs
Veja na primeira linha acima por que usamos **`-t 1 -W 1 -V`** ao validar controles de bloqueio como Fail2ban e `pam_faillock`: com `-t 1` (1 única thread sequencial), `-W 1` (1 segundo de intervalo entre cada tentativa) e `-V` (mostra cada tentativa `login+pass` na tela), você observa exatamente em qual tentativa (`Attempt 5 of 6`) a conexão passa a ser recusada pelo firewall (`Connection refused` / `Timeout`), comprovando com precisão cirúrgica a eficácia do controle!

## Como verificar
Integre esse teste em pipelines de validação de infraestrutura (*Security Chaos Engineering* / *Continuous Security Validation*) sempre que atualizar configurações de `sshd_config`, PAM ou Ingress/WAF.

## Conexões
- [[thc-hydra-auditoria-email-diretorio-smtp-enum-imap-pop3-ldap-tls]] — Veja também: Auditando Serviços de E-mail e Diretório no THC-Hydra: Enumeração de Contas **`smtp-enum` (`VRFY`/`EXPN`/`RCPT TO`)**, **`smtp`**, **`imap`/`pop3`** e **`ldap3` (`-S` LDAPS)**.
- [[thc-hydra-deteccao-forense-redes-user-agent-padrao-conexoes-suricata-zeek]] — Veja também: Engenharia de Detecção (**Blue Team / SOC / NIDS / SIEM**) Contra Ataques do **THC-Hydra**: `User-Agent` Default (`Mozilla/4.0 (Hydra)`), Padrões de Conexão e Correlação.
- [[thc-hydra-arquitetura-auditoria-autenticacao-rede-paralela-modulos]] — Referência cruzada direta com thc-hydra-arquitetura-auditoria-autenticacao-rede-paralela-modulos.

## Fontes
- [THC-Hydra Official Documentation (`vanhauser-thc/thc-hydra/master/README`)](https://raw.githubusercontent.com/vanhauser-thc/thc-hydra/master/README) — documentação oficial do THC-Hydra detalhando protocolos suportados, sintaxe URI `PROTOCOL://TARGET:PORT/OPTIONS`, listas `-M` e inspeção de módulos `hydra -U`; consultado em 2026-10-03.
- [Official `hydra(1)` Manpage Specification (`vanhauser-thc/thc-hydra/master/hydra.1`)](https://raw.githubusercontent.com/vanhauser-thc/thc-hydra/master/hydra.1) — manpage oficial `hydra(1)` detalhando flags `-l`/`-L`, `-p`/`-P`, `-C`, `-e nsr`, `-u`, `-f`/`-F`, `-t`/`-T`, `-w`/`-W`/`-c`, `-R`, `-b json` e o utilitário `pw-inspector`; consultado em 2026-10-03.
