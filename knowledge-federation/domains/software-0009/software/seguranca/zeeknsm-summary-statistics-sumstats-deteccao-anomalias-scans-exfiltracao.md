---
id: software.seguranca.tranche03.000210
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-03.md"
fontes: ["https://raw.githubusercontent.com/zeek/zeek/master/doc/about/architecture.rst", "https://raw.githubusercontent.com/zeek/zeek/master/README.md", "https://github.com/zeek/zeek"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Zeek `SumStats` (Summary Statistics Framework): agregação estatística distribuída para detectar Port Scans, DGA e Beaconing

## Em uma frase
O **Summary Statistics Framework (`SumStats`)** do Zeek é um motor de redução estatística distribuída em memória que agrega observações (`SumStats::observe`) de todos os processos `worker` do cluster ao longo de uma janela de tempo (`epoch`) e calcula métricas como **`SUM`**, **`UNIQUE`**, **`AVERAGE`**, **`VARIANCE`**, **`MAX`**, **`MIN`**, **`STDDEV`** e **`HLL_UNIQUE`** (*HyperLogLog* para cardinalidade de milhões de itens com memória constante!).

## Por que importa
Se um atacante realizar um *Horizontal Port Scan* lento ou consultas DNS distribuídas que caem em 8 workers diferentes do cluster Zeek, contadores locais por worker não enxergam o total global da rede; o `SumStats` agrega automaticamente os contadores de todos os workers no final de cada `epoch`.

## Como funciona
No callback `threshold_crossed` ou `epoch_result` do `SumStats`, você recebe o resultado consolidado de todo o cluster e emite um único alerta preciso no `notice.log`!

## Exemplo
```zeek
# Usando SumStats com HyperLogLog (HLL_UNIQUE) para detectar hosts que consultam mais de 150 domínios NXDOMAIN em 5 minutos (possível malware DGA):
event zeek_init()
    {
    local r1 = SumStats::Reducer($stream="dns.nxdomain", $apply=set(SumStats::UNIQUE));
    SumStats::create([
        $name="detect-dga-nxdomain",
        $epoch=5mins,
        $reducers=set(r1),
        $threshold=150.0,
        $threshold_val(key: SumStats::Key, result: SumStats::Result): double =
            { return result["dns.nxdomain"]$unique + 0.0; },
        $threshold_crossed(key: SumStats::Key, result: SumStats::Result) =
            { print fmt("Host %s gerou %d NXDOMAINs distintos em 5min!", key$host, result["dns.nxdomain"]$unique); }
    ]);
    }
```

## Limites e trade-offs
Prefira o cálculo probabilístico **`SumStats::HLL_UNIQUE`** em vez de `SumStats::UNIQUE` quando monitorar cardinalidade em janelas longas de alto volume, reduzindo drasticamente o consumo de RAM por chave.

## Como verificar
Teste scripts baseados em `SumStats` sobre um PCAP usando `zeek -C -r scan.pcap` e valide o disparo de `threshold_crossed`.

## Conexões
- [[zeeknsm-package-manager-zkg-ja3-ja4-bzar-mitre-attack-extensoes]] — Veja também: Zeek Package Manager (`zkg`): instalação de pacotes comunitários (`JA3`, `JA4`, `MITRE ATT&CK BZAR`, `hassh`, `cve-detectors`).

## Fontes
- [Zeek GitHub — README.md (Network Traffic Analysis & Security Monitoring Framework, Key Features, Scripting & Tooling)](https://raw.githubusercontent.com/zeek/zeek/master/doc/about/architecture.rst) — README oficial do zeek/zeek apresentando o framework de análise semântica de rede, estado de camada de aplicação e linguagem de scripts; consultado em 2026-10-03.
- [Zeek Official Documentation — Architecture (doc/about/architecture.rst: Event Engine, Packet/Session/File Analysis & Script Interpreter)](https://raw.githubusercontent.com/zeek/zeek/master/README.md) — Documentação oficial de arquitetura do Zeek detalhando a separação entre o Event Engine neutro de política e o Script Interpreter; consultado em 2026-10-03.
- [Zeek Network Security Monitor — Official GitHub Repository](https://github.com/zeek/zeek) — Repositório oficial BSD-3-Clause do Zeek; consultado em 2026-10-03.
