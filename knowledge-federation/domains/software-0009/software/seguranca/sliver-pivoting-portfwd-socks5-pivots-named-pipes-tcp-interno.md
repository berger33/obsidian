---
id: software.seguranca.tranche16.001546
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
fontes: ["https://raw.githubusercontent.com/BishopFox/sliver/master/README.md", "https://sliver.sh/docs?name=Getting+Started"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Pivoting e Movimentação Lateral no Sliver: **`socks5` In-Memory**, **`portfwd`**, **`rportfwd`** e **Internal Peer-to-Peer Pivots (`pivots named-pipe` / `tcp`)**

## Em uma frase
Imagine que você obteve um implante Sliver em um servidor web na DMZ (`Host A`), mas o banco de dados ou Domain Controller (`Host B`) na rede interna **não tem nenhum acesso de saída para a internet** (ele só aceita conexões vindas do `Host A`). Como alcançar o `Host B` e até mesmo controlar um segundo implante no `Host B` encadeando o tráfego por dentro do `Host A`?

## Por que importa
O Sliver oferece **3 mecanismos nativos de Pivoting**: **(1) `portfwd add` e `rportfwd`** — encaminhamento direto de portas TCP locais/remotas pelo túnel C2; **(2) `socks5 start`** — abre um proxy **SOCKS5 em memória** na estação do operador roteado pelo implante (sem subir nenhuma porta nova no host alvo!); e **(3) `pivots` (*Peer-to-Peer Implant Pivoting*)**!

## Como funciona
Com **`pivots named-pipe --bind MeuPipe`** (SMB Named Pipes no Windows) ou **`pivots tcp --lport 9000`** no `Host A`, você gera um implante especial (`generate --named-pipe ...` ou `--tcp-pivot ...`) para o `Host B`: o implante do `Host B` se conecta internamente ao `Host A`, e o `Host A` **encaminha todo o tráfego C2 criptografado ponta a ponta do `Host B` para o servidor Sliver na internet**!

## Exemplo
```text
# Abrir um proxy SOCKS5 local (127.0.0.1:1080) e um Port Forward TCP sobre uma sessao ativa do Sliver e configurar um Pivot P2P
sliver (PROPER_ANTHONY) > socks5 start -H 127.0.0.1 -P 1080
sliver (PROPER_ANTHONY) > portfwd add -b 127.0.0.1:8445 -r 10.20.30.10:445
sliver (PROPER_ANTHONY) > pivots tcp --bind 0.0.0.0 --lport 9898
```

## Limites e trade-offs
Atenção ao detalhe documentado no guia oficial (`Getting Started`): comandos de tunelamento em tempo real como **`socks5`**, **`portfwd`** e **`pivots`** exigem uma **Session ativa** (se você estiver em um **Beacon**, basta rodar `interactive` primeiro para abrir a Session e depois iniciar o `socks5` ou `portfwd`)!

## Como verificar
E como do lado da defesa (Blue Team) você detecta um **Pivot P2P por Named Pipe SMB (`pivots named-pipe`)** entre duas estações Windows? Monitorando os eventos **Sysmon Event ID 17 (`PipeEvent — Pipe Created`) e Event ID 18 (`PipeEvent — Pipe Connected`)** junto com conexões SMB horizontais estação-para-estação na porta `445`!

## Conexões
- [[sliver-execucao-em-memoria-bof-coff-execute-assembly-sideload-spawndll]] — Veja também: Pós-Exploração *In-Memory* no Sliver: **BOF / COFF Loader (`Armory`)**, **`execute-assembly` (.NET CLR)**, **`sideload`** e **`spawndll`** sem Tocar o Disco.
- [[sliver-compilacao-ofuscacao-garble-stagers-shellcode-external-builders]] — Veja também: Compilação Avançada de Implantes no Sliver: Ofuscação de Símbolos (**`garble`**), Formatos (`executable`, `shared-lib`, `service`, `shellcode`), **Stagers** e **External Builders**.
- [[sliver-arquitetura-c2-emulacao-adversarios-mtls-wireguard-http-dns]] — Referência cruzada direta com sliver-arquitetura-c2-emulacao-adversarios-mtls-wireguard-http-dns.
- [[sliver-modos-operacao-beacon-assincrono-jitter-vs-session-interativa]] — Referência cruzada direta com sliver-modos-operacao-beacon-assincrono-jitter-vs-session-interativa.
- [[ligolo-arquitetura-tunelamento-camada-3-tun-gvisor-sem-socks]] — Referência cruzada direta com ligolo-arquitetura-tunelamento-camada-3-tun-gvisor-sem-socks.

## Fontes
- [Sliver Adversary Emulation Framework Official Repository (`BishopFox/sliver`)](https://raw.githubusercontent.com/BishopFox/sliver/master/README.md) — repositório oficial do framework C2 Sliver em Go cobrindo implantes multi-plataforma, chaves assimétricas únicas por binário e execução BOF/COFF; consultado em 2026-10-03.
- [Sliver Official Documentation — Getting Started (`sliver.sh/docs?name=Getting+Started`)](https://sliver.sh/docs?name=Getting+Started) — documentação oficial do Sliver detalhando arquitetura Server/Multiplayer, diferença entre `Beacon Mode` e `Session Mode`, geração de implantes, `interactive` e Stagers; consultado em 2026-10-03.
