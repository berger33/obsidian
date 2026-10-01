# Inventário legado de 1 milhão — estado de qualidade

O checkpoint e os pacotes materializados do merge preservam **1.000.000 de registros virtuais** e uma sequência de lotes com esse número de arquivos. A auditoria atual identificou texto-template em todos os registros virtuais. Portanto, esses artefatos representam uma **meta de inventário/materialização**, não 1.000.000 de notas válidas.

## Estado auditado em 2026-10-01

- Registros virtuais no SQLite: **1.000.000**.
- Registros com marcadores de conteúdo-template: **1.000.000**.
- Caminhos virtuais marcados como materializados no checkpoint: **8.000**.
- Notas físicas do lote inicial: **100**, sem status profundo/revisado no schema legado.
- Notas ativas novas que passaram pelo gate automatizado: **8 candidatas**; revisão humana pendente.
- Notas plenamente aprovadas por revisão humana: **0**.

As quantidades `1.015.600`, `15.600`, `5.000 lotes` e `1.021.127 entradas` em manifestos antigos são contagens de arquivos e registros. Não devem ser usadas como contagem de conhecimento editorialmente validado.

## Artefatos

```text
archives/merge-completo-materializado-1m.tar.xz
archives/study-vault-1m-packs.zip
archives/ledger-v1000000-mat8000.sqlite.xz
```

Os pacotes permanecem disponíveis por compatibilidade e recuperação. A auditoria em [`exports/reports/note-quality-audit.md`](exports/reports/note-quality-audit.md) separa catálogo, arquivos candidatos e revisão humana.

## Auditoria reproduzível

```bash
python3 -m unittest discover -s knowledge-federation/tests -v
python3 knowledge-federation/scripts/audit_note_quality.py \
  --path knowledge-federation/domains \
  --archive knowledge-federation/archives/ledger-v1000000-mat8000.sqlite.xz
```

Um passe automatizado apenas libera a nota para revisão humana. Só após checagem das fontes e aprovação registrada em `revisao_humana`/`revisor` ela entra na contagem de notas válidas.
