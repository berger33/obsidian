---
id: software.seguranca.tranche16.001545
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

# Pós-Exploração *In-Memory* no Sliver: **BOF / COFF Loader (`Armory`)**, **`execute-assembly` (.NET CLR)**, **`sideload`** e **`spawndll`** sem Tocar o Disco

## Em uma frase
Por que um operador experiente do Sliver **JAMAIS abre um `shell` interativo (`cmd.exe` / `powershell.exe` / `/bin/bash`) nem grava ferramentas `.exe` no disco do alvo**, preferindo usar os carregadores em memória do Sliver (**BOF/COFF, `execute-assembly`, `sideload` e `spawndll`)**?

## Por que importa
Porque criar processos filhos como `cmd.exe` ou `whoami.exe` gera imediatamente eventos **Sysmon Event ID 1 (`Process Creation` — código `4688`)** que qualquer regra básica de **Sigma / Hayabusa /Chainsaw / EDR** detecta em 1 segundo!

## Como funciona
Para operar em memória (*In-Memory Execution*), o Sliver suporta nativamente: **(1) Execução de `BOF / COFF` (*Beacon Object Files*)** em `amd64` e `arm64` (executando código C compilado dentro do próprio processo do implante sem criar nenhum processo novo!); **(2) `execute-assembly`** (carrega o runtime `.NET CLR` em memória para rodar ferramentas C# como Certipy/SharpHound/Rubeus); **(3) `sideload`** (converte DLLs/binários nativos em shellcode reflexivo via *Donut*); e **(4) Gerenciador de Pacotes `armory`**!

## Exemplo
```text
# Instalar extensoes BOF/C# pelo gerenciador oficial Armory do Sliver e executar comandos diretamente na memoria do implante
sliver > armory
sliver > armory install all
sliver (PROPER_ANTHONY) > ps
sliver (PROPER_ANTHONY) > getprivs
```

## Limites e trade-offs
Veja na seção *System Requirements* e *Architecture* da documentação oficial que os comandos nativos do implante Sliver (como **`ls`, `pwd`, `cat`, `download`, `upload`, `ps`, `netstat`, `ifconfig`, `getuid`, `getprivs`, `procdump`**) são **implementados diretamente em chamadas de API/Syscalls do Go dentro do próprio implante** — eles **NÃO invocam `/bin/ls`, `ps` ou `netstat.exe` no sistema operacional**!

## Como verificar
E ao usar `execute-assembly` ou `spawndll` no Windows, o Sliver permite customizar o processo sacrificial (`--process`) e aplicar spoofing de Parent PID (`--ppid`) para testar se o EDR da empresa detecta injeção de processos e carregamento anômalo de `clr.dll` (Sysmon Event ID 7 e 8)!

## Conexões
- [[sliver-modo-multiplayer-operadores-grpc-mtls-rbac-auditoria-logs]] — Veja também: Operação em Equipe (**Multiplayer Mode** sobre gRPC mTLS), Gerenciamento de Operadores (**`new-operator`**) e **Audit Log JSON** Completo para Purple Team no Sliver.
- [[sliver-pivoting-portfwd-socks5-pivots-named-pipes-tcp-interno]] — Veja também: Pivoting e Movimentação Lateral no Sliver: **`socks5` In-Memory**, **`portfwd`**, **`rportfwd`** e **Internal Peer-to-Peer Pivots (`pivots named-pipe` / `tcp`)**.
- [[sliver-arquitetura-c2-emulacao-adversarios-mtls-wireguard-http-dns]] — Referência cruzada direta com sliver-arquitetura-c2-emulacao-adversarios-mtls-wireguard-http-dns.

## Fontes
- [Sliver Adversary Emulation Framework Official Repository (`BishopFox/sliver`)](https://raw.githubusercontent.com/BishopFox/sliver/master/README.md) — repositório oficial do framework C2 Sliver em Go cobrindo implantes multi-plataforma, chaves assimétricas únicas por binário e execução BOF/COFF; consultado em 2026-10-03.
- [Sliver Official Documentation — Getting Started (`sliver.sh/docs?name=Getting+Started`)](https://sliver.sh/docs?name=Getting+Started) — documentação oficial do Sliver detalhando arquitetura Server/Multiplayer, diferença entre `Beacon Mode` e `Session Mode`, geração de implantes, `interactive` e Stagers; consultado em 2026-10-03.
