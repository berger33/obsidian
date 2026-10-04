---
id: software.seguranca.tranche12.001159
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
fontes: ["https://raw.githubusercontent.com/cowrie/cowrie/main/README.rst", "https://raw.githubusercontent.com/cowrie/cowrie/main/src/cowrie/data/etc/cowrie.cfg.dist"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Emulação Dinâmica de Comandos com **IA Generativa (`backend = llm`)** no Cowrie: Como Responder a Qualquer Comando Inédito do Atacante

## Em uma frase
Qual é a maior limitação histórica de honeypots de média interação baseados em emulação tradicional (`backend = shell`)? Se o atacante digitar um comando ou pipeline complexo para o qual o Cowrie não possui um handler Python programado (por exemplo, `kubectl get secrets -A`, `docker ps --format '{{.Names}}'`, `psql -U postgres -c '\l'` ou um script awk customizado), o emulador tradicional responde `bash: command not found` — revelando ou limitando a interação!

## Por que importa
Para superar essa barreira sem precisar manter um pool pesado de VMs reais (`backend = proxy`), o Cowrie introduziu o **backend `llm` (`backend = llm`)**!

## Como funciona
Quando `backend = llm` está ativo e configurado no bloco `[llm]` do `etc/cowrie.cfg`, o Cowrie envia os comandos do atacante para um modelo de linguagem (LLM via API ou modelo local compatível) com um *system prompt* estrito que instrui o modelo a agir exatamente como um terminal Linux Debian/Ubuntu daquele host, mantendo o histórico de contexto da sessão (arquivos criados, diretório atual `pwd`, variáveis definidas) e gerando saídas de terminal realistas para qualquer ferramenta invocada!

## Exemplo
```ini
# Estrutura conceitual de configuracao do backend LLM experimental no etc/cowrie.cfg
[honeypot]
backend = llm
hostname = prd-k8s-ctrl-01

[llm]
model = gpt-4o-mini
```

## Limites e trade-offs
Mesmo quando opera no modo `llm`, o Cowrie preserva todas as suas capacidades nativas de segurança e auditoria: autenticação controlada, registro estruturado em `cowrie.json`, gravação de `ttylog` para replay com `playlog` e interceptação de downloads.

## Como verificar
Ao experimentar `backend = llm`, configure limites estritos de tokens, *rate limiting* por IP e *timeouts* de sessão (`idle_timeout`) para evitar que um bot automatizado gere custos excessivos de inferência de API.

## Conexões
- [[cowrie-anti-fingerprinting-disfarce-honeypot-banners-uptime-rede]] — Veja também: Técnicas de **Anti-Fingerprinting** no Cowrie: Como Evitar que Atacantes e Scanners Identifiquem que o Servidor é um Honeypot.
- [[cowrie-deception-engineering-intranet-deteccao-movimentacao-lateral-ssh]] — Veja também: Engenharia de Deception na **Rede Interna (Intranet)** com Cowrie: Transformando Tentativas de Movimentação Lateral SSH em Alertas de Alta Fidelidade.
- [[cowrie-arquitetura-honeypot-ssh-telnet-shell-proxy-llm]] — Referência cruzada direta com cowrie-arquitetura-honeypot-ssh-telnet-shell-proxy-llm.
- [[cowrie-sistema-arquivos-falso-fs-pickle-fsctl-createfs-honeyfs]] — Referência cruzada direta com cowrie-sistema-arquivos-falso-fs-pickle-fsctl-createfs-honeyfs.
- [[cowrie-modo-proxy-alta-interacao-backend-pool-qemu-libvirt]] — Referência cruzada direta com cowrie-modo-proxy-alta-interacao-backend-pool-qemu-libvirt.

## Fontes
- [Cowrie Official GitHub (`README.rst`) — Medium to High Interaction SSH and Telnet Honeypot](https://raw.githubusercontent.com/cowrie/cowrie/main/README.rst) — documentação oficial do Cowrie cobrindo os modos `shell`, `proxy` e `llm`, sistema de arquivos falso `fs.pickle`, utilitários `fsctl`/`createfs`/`playlog` e logs JSON; consultado em 2026-10-03.
- [Cowrie Official Configuration Reference (`src/cowrie/data/etc/cowrie.cfg.dist`)](https://raw.githubusercontent.com/cowrie/cowrie/main/src/cowrie/data/etc/cowrie.cfg.dist) — especificação completa dos parâmetros de configuração do Cowrie (`[honeypot]`, `auth_class`, `UserDB`, `AuthRandom`, `ttylog`, `download_limit_size`, `[backend_pool]`); consultado em 2026-10-03.
